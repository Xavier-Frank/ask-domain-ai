from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    """
    Represents a semantic search request.
    """

    question: str = Field(
        ...,
        description="Natural language question."
    )

    top_k: int = Field(
        default=20,
        ge=1,
        le=20,
        description="Number of chunks to retrieve."
    )