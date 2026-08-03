import httpx

from app.configs.ollama_config import (
    OLLAMA_MODEL, OLLAMA_TIMEOUT, OLLAMA_URL
)
from app.models.llm.response.llm_response import LLMResponse
from app.models.llm.response.llm_source import LLMSource
from app.models.prompt.prompt_request import PromptRequest


class OllamaService:
    """"
    Generate prompt to ollama and returns generated answer
    """

    @classmethod
    def generate(cls, request: PromptRequest) -> LLMResponse:

        response = httpx.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": request.prompt,
                "stream": False
            },
            timeout=OLLAMA_TIMEOUT
        )

        print("Status:", response.status_code)
        print("Response:", response.text)

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

    @staticmethod
    def _build_sources(
            request: PromptRequest,
    ) -> list[LLMSource]:
        """
        Convert retrieved search results into LLM response sources.
        """

        return [
            LLMSource(
                filename=result.filename,
                start_page=result.start_page,
                end_page=result.end_page,
                chunk_id=result.chunk_id,
            )
            for result in request.sources
        ]
