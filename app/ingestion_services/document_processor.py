from pathlib import Path
from datetime import datetime
import time
import uuid

from app.models.document_models import Document
from app.ingestion_services.chunk_service import ChunkService
from app.ingestion_services.pdf_service import PdfService


class DocumentProcessor:
    """
    Coordinates the document ingestion pipeline.
    """

    @staticmethod
    def ingest(path: Path) -> Document:

        start = time.perf_counter()

        document_id = str(uuid.uuid4())

        pages = PdfService.extract_pages(path)

        chunk_service = ChunkService(
            max_chars=1000,
            overlap_sentences=3
        )

        chunks = chunk_service.create_chunks(document_id, pages)

        duration = time.perf_counter() - start

        return Document(
            id=str(uuid.uuid4()),
            filename=path.name,
            path=str(path),
            uploaded_at=datetime.utcnow(),
            page_count=len(pages),
            character_count=sum(len(page.text) for page in pages),
            chunk_count=len(chunks),
            processing_time=duration,
            chunks=chunks
        )