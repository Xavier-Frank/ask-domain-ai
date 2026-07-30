# this service handles the document upload
from fastapi import APIRouter, UploadFile, File, HTTPException
from starlette import status

from app.services.pdf_service import PdfService

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

    text = PdfService.extract_text_from_pdf(saved_path)

    return {
        "filename": file.filename,
        "characters": len(text),
        "preview": text[:500]
    }
