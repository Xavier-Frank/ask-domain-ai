import re

from app.models.document_sentence import DocumentSentence


class SentenceService:
    """
    Responsible for splitting extracted document text into individual
    sentences while preserving the originating page number.
    """

    SENTENCE_PATTERN = re.compile(r"(?<=[.!?])\s+")

    @classmethod
    def split(
        cls,
        text: str,
        page_number: int
    ) -> list[DocumentSentence]:
        """
        Split a page's text into individual sentences.

        Args:
            text: Extracted text from a document page.
            page_number: Page number the text originated from.

        Returns:
            A list of DocumentSentence objects.
        """

        # Normalize whitespace
        normalized_text = re.sub(r"\s+", " ", text).strip()

        if not normalized_text:
            return []

        sentences = cls.SENTENCE_PATTERN.split(normalized_text)

        return [
            DocumentSentence(
                text=sentence.strip(),
                page_number=page_number
            )
            for sentence in sentences
            if sentence.strip()
        ]