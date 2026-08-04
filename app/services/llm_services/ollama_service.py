import json

import httpx

from app.configs.ollama_config import (
    OLLAMA_MODEL,
    OLLAMA_TIMEOUT,
    OLLAMA_URL,
)
from app.models.llm.response.llm_response import LLMResponse
from app.models.llm.response.llm_source import LLMSource
from app.models.prompt.prompt_request import PromptRequest


class OllamaService:
    """
    Service responsible for communicating with the configured
    Ollama model.

    Supports both:

    - Standard request/response generation
    - Server-Sent Event (SSE) streaming
    """

    @classmethod
    def generate(
        cls,
        request: PromptRequest,
    ) -> LLMResponse:
        """
        Generate a complete response from Ollama.

        Args:
            request: Prompt request ready for the LLM.

        Returns:
            LLMResponse
        """

        response = httpx.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": request.prompt,
                "stream": False,
            },
            timeout=OLLAMA_TIMEOUT,
        )

        response.raise_for_status()

        body = response.json()

        return LLMResponse(
            question=request.question,
            answer=body["response"].strip(),
            model=body["model"],
            prompt_tokens=body.get("prompt_eval_count"),
            completion_tokens=body.get("eval_count"),
            sources=cls._build_sources(request),
        )

    @classmethod
    def generate_stream(
            cls,
            request: PromptRequest,
    ):
        """
        Stream tokens from Ollama using Server-Sent Events.
        """

        try:

            with httpx.stream(
                    "POST",
                    f"{OLLAMA_URL}/api/generate",
                    json={
                        "model": OLLAMA_MODEL,
                        "prompt": request.prompt,
                        "stream": True,
                    },
                    timeout=None,
            ) as response:

                response.raise_for_status()

                # -----------------------------
                # Start Event
                # -----------------------------

                yield cls._sse(
                    {
                        "type": "start",
                        "model": OLLAMA_MODEL,
                        "question": request.question,
                    }
                )

                for line in response.iter_lines():

                    if not line:
                        continue

                    body = json.loads(line)

                    print("body:", body)

                    # -----------------------------
                    # Token Event
                    # -----------------------------

                    token = body.get("response")

                    if token:
                        yield cls._sse(
                            {
                                "type": "token",
                                "content": token,
                            }
                        )

                    # -----------------------------
                    # Finished Generation
                    # -----------------------------

                    if body.get("done"):
                        yield cls._sse(
                            {
                                "type": "sources",
                                "sources": [
                                    source.model_dump()
                                    for source in cls._build_sources(request)
                                ],
                            }
                        )

                        yield cls._sse(
                            {
                                "type": "usage",
                                "model": body.get("model"),
                                "prompt_tokens": body.get("prompt_eval_count"),
                                "completion_tokens": body.get("eval_count"),
                                "total_duration": body.get("total_duration"),
                                "load_duration": body.get("load_duration"),
                                "eval_duration": body.get("eval_duration"),
                            }
                        )

                        yield cls._sse(
                            {
                                "type": "complete",
                                "success": True,
                            }
                        )
                        return

        except httpx.HTTPError as ex:

            yield cls._sse(
                {
                    "type": "error",
                    "message": str(ex),
                }
            )

        except Exception as ex:

            yield cls._sse(
                {
                    "type": "error",
                    "message": str(ex),
                }
            )

    @staticmethod
    def _build_sources(
        request: PromptRequest,
    ) -> list[LLMSource]:
        """
        Convert retrieved chunks into response sources.
        """

        return [
            LLMSource(
                filename=result.filename,
                chunk_id=result.chunk_id,
                start_page=result.start_page,
                end_page=result.end_page,
            )
            for result in request.sources
        ]

    @staticmethod
    def _sse(data: dict) -> str:
        """
        Convert a dictionary into a valid Server-Sent Event.

        Example:

        data: {"type":"token","content":"Hello"}

        """

        return f"data: {json.dumps(data)}\n\n"