# this service handles the document upload
from fastapi import APIRouter, UploadFile, File, HTTPException
from starlette import status

from app.services.ingestion_services.document_processor import DocumentProcessor
from app.services.ingestion_services.pdf_service import PdfService

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/upload", tags=["Documents"])
async def upload_document(file: UploadFile = File(...)):

    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Provide a valid pdf file"
        )

    if not file.filename.endswith((".pdf", ".PDF")):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are accepted"
        )

    file_bytes = await file.read()


    saved_path = PdfService.save_pdf(
        file.filename,
        file_bytes
    )

    document = DocumentProcessor.ingest(saved_path)

    return {
        "filename": document.filename,
        "pages": document.page_count,
        "chunks": len(document.chunks),
        "characters": document.character_count,
        "sample_chunk": document.chunks
    }
