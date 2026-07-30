from dataclasses import dataclass


@dataclass
class DocumentSentence:
    text: str
    page_number: int