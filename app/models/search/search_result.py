from pydantic import BaseModel, Field


class SearchResult(BaseModel):
    """
    Represents retrieved chunk
    """
    chunk_id: int = Field(
        title="Chunk ID"
    )

    text: str = Field(
        description="Text of the chunk"
    )

    similarity: float = Field(
        description="Similarity score of the chunk"
    )

    start_page: int = Field(
        description="Start page of the chunk"
    )

    end_page: int = Field(
        description="End page of the chunk"
    )

    filename: str = Field(
        description="Document filename"
    )