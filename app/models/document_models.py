from datetime import datetime

from pydantic import BaseModel, Field

from app.models.document_chunk import DocumentChunk


class Document(BaseModel):
    """
    Represents an uploaded document and all metadata generated during
    the ingestion pipeline.
    """

    # ---------- Identity ----------
    id: str = Field(
        description="Unique identifier for the document."
    )

    filename: str = Field(
        description="Original filename."
    )

    path: str = Field(
        description="Location of the stored PDF."
    )

    # ---------- Upload Metadata ----------
    uploaded_at: datetime = Field(
        description="UTC timestamp when the document was processed."
    )

    # ---------- Document Statistics ----------
    page_count: int = Field(
        ge=0,
        description="Total number of pages."
    )

    character_count: int = Field(
        ge=0,
        description="Total number of extracted characters."
    )

    chunk_count: int = Field(
        ge=0,
        description="Number of generated chunks."
    )

    processing_time: float = Field(
        ge=0,
        description="Time taken to process the document in seconds."
    )

    # ---------- Processed Data ----------
    chunks: list[DocumentChunk] = Field(
        default_factory=list,
        description="Sentence-aware chunks extracted from the document."
    )