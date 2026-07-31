from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DOCUMENTS_DIR = BASE_DIR / "documents"

UPLOAD_DIR = DOCUMENTS_DIR / "uploads"

CHROMA_DB_DIR = DOCUMENTS_DIR / "chroma_db"
