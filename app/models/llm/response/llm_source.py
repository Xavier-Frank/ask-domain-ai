from pydantic import BaseModel


class LLMSource(BaseModel):
    filename: str | None = None
    start_page: int = None
    end_page: int = None