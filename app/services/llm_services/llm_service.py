from app.models.llm.response.llm_response import LLMResponse
from app.models.prompt.prompt_request import PromptRequest
from app.services.llm_services.ollama_service import OllamaService


class LLMService:
    """
    Facade for calling a response llm model
    """

    @classmethod
    def generate(
            cls,
            prompt: PromptRequest
    ) -> LLMResponse:
        return OllamaService.generate(prompt)