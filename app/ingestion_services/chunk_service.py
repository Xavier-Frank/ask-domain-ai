from app.ingestion_services.sentence_service import SentenceService
from app.ingestion_services.text_cleaner import TextCleaner
from app.models.document_chunk import DocumentChunk
from app.models.document_sentence import DocumentSentence
from app.models.pdf_models import DocumentPage


class ChunkService:
    """
    Responsible for converting an entire document into semantically
    meaningful, sentence-aware chunks.

    Unlike a page-based chunker, this implementation allows chunks to span
    multiple pages while preserving the original page metadata.
    """

    def __init__(
        self,
        max_chars: int = 800,
        overlap_sentences: int = 2
    ):
        self.max_chars = max_chars
        self.overlap_sentences = overlap_sentences

    def create_chunks(
        self,
        document_id: str,
        pages: list[DocumentPage]
    ) -> list[DocumentChunk]:
        """
        Create sentence-aware chunks from an entire document.

        Args:
            document_id: Unique identifier of the document.
            pages: Extracted document pages.

        Returns:
            A list of DocumentChunk objects.
        """

        # ---------------------------------------------------------
        # Flatten all pages into one continuous sentence stream.
        # ---------------------------------------------------------

        all_sentences: list[DocumentSentence] = []

        for page in pages:

            cleaned_text = TextCleaner.clean(page.text)

            all_sentences.extend(
                SentenceService.split(
                    text=cleaned_text,
                    page_number=page.page_number
                )
            )

        chunks: list[DocumentChunk] = []

        current_sentences: list[DocumentSentence] = []
        current_size = 0
        chunk_id = 1

        for sentence in all_sentences:

            sentence_length = len(sentence.text) + 1

            if (
                current_sentences
                and current_size + sentence_length > self.max_chars
            ):

                chunks.append(
                    self._build_chunk(
                        chunk_id=chunk_id,
                        document_id=document_id,
                        sentences=current_sentences
                    )
                )

                chunk_id += 1

                # Preserve sentence overlap to maintain context.
                current_sentences = current_sentences[
                    -self.overlap_sentences:
                ]

                current_size = len(
                    " ".join(
                        sentence.text
                        for sentence in current_sentences
                    )
                )

            current_sentences.append(sentence)
            current_size += sentence_length

        # Persist the final chunk.
        if current_sentences:

            chunks.append(
                self._build_chunk(
                    chunk_id=chunk_id,
                    document_id=document_id,
                    sentences=current_sentences
                )
            )

        return chunks

    @staticmethod
    def _build_chunk(
        chunk_id: int,
        document_id: str,
        sentences: list[DocumentSentence]
    ) -> DocumentChunk:
        """
        Construct a DocumentChunk from a collection of document sentences.
        """

        text = " ".join(
            sentence.text
            for sentence in sentences
        )

        return DocumentChunk(
            chunk_id=chunk_id,
            document_id=document_id,
            start_page=sentences[0].page_number,
            end_page=sentences[-1].page_number,
            text=text,
            character_count=len(text),
            sentence_count=len(sentences)
        )