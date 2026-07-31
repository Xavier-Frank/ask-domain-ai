from pydantic import BaseModel, Field

from app.models.search.search_result import SearchResult


class RetrievalContext(BaseModel):
    """
    Represents the final context prepared for the LLM
    """

    question: str = Field(
        description="Users original question"
    )

    prompt: str = Field(
        description="Fully constructed prompt for the LLM"
    )

    source: list[SearchResult] = Field(
        description="Source Chunks used to construct the prompt"
    )