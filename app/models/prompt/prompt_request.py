from pydantic import BaseModel

from app.models.search.search_result import SearchResult


class PromptRequest(BaseModel):
    question: str
    prompt: str
    sources: list[SearchResult]