from pydantic import BaseModel, Field

from app.models.llm.response.llm_source import LLMSource


class LLMResponse(BaseModel):
    question: str
    answer: str
    model: str
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    sources: list[LLMSource] = Field(default_factory=list)