from pydantic import BaseModel


class LLMResponse(BaseModel):
    answer: str
    model: str
    prompt_tokens: int | None = None
    completion_tokens: int | None = None