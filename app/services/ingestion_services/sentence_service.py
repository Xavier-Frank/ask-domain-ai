import re

from app.models.ingestion.document_sentence import DocumentSentence


class SentenceService:
    """
    Splits cleaned document text into sentences.
    """

    SENTENCE_PATTERN = re.compile(r"(?<=[.!?])\s+")

    @classmethod
    def split(
        cls,
        text: str,
        page_number: int
    ) -> list[DocumentSentence]:

        if not text.strip():
            return []

        return [
            DocumentSentence(
                text=sentence.strip(),
                page_number=page_number
            )
            for sentence in cls.SENTENCE_PATTERN.split(text)
            if sentence.strip()
        ]