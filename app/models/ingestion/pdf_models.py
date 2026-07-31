from pydantic import BaseModel, Field


class DocumentPage(BaseModel):
    """
    Represents a single page extracted from a PDF document.
    """

    page_number: int = Field(
        ge=1,
        description="The one-based page number of the page within the original PDF document."
    )

    text: str = Field(
        description="The textual content extracted from the PDF page."
    )