from pydantic import BaseModel, Field


class DocumentChunk(BaseModel):
    """
    Represents a semantically meaningful chunk of text extracted from a document.
    """

    chunk_id: int = Field(
        description="Sequential identifier assigned to the chunk within the processed document."
    )

    document_id: str = Field(
        description="Unique identifier of the document this chunk belongs to."
    )

    start_page: int = Field(
        ge=1,
        description="The page number where this chunk begins in the original document."
    )

    end_page: int = Field(
        ge=1,
        description="The page number where this chunk ends in the original document."
    )

    text: str = Field(
        description="The extracted chunk text that will be embedded and used for semantic search."
    )

    character_count: int = Field(
        ge=0,
        description="Total number of characters contained in this chunk."
    )

    sentence_count: int = Field(
        ge=0,
        description="Total number of sentences contained in this chunk."
    )

    embedding: list[float] | None = Field(
        default=None,
        description="Vector embedding generated from the chunk text. This is populated during the embedding stage."
    )