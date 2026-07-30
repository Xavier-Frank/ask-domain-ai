## this service helps to save file, read, and extract texts from pdfs
from pathlib import Path

import fitz

from app.models.pdf_models import DocumentPage

UPLOAD_FOLDER = Path("documents/uploads")

class PdfService:

    @staticmethod
    def save_pdf(file_name: str, file_bytes: bytes) -> Path:
        """
            Save a pdf file to disk
            :param file_name: name of the file
            :param file_bytes: file in bytes
            :return: the file destination
        """

        UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

        destination = UPLOAD_FOLDER / file_name

        with open(destination, "wb") as file:
            file.write(file_bytes)

        return destination


    @staticmethod
    def extract_text_from_pdf(pdf_path: Path) -> str:
        """
            Extract text from every page of a pdf file
            :param pdf_path: represents the location of the pdf
            :return: text
        """
        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    @staticmethod
    def extract_pages(path):
        document = fitz.open(path)

        pages = []

        for page_number, page in enumerate(document):

            pages.append(
                DocumentPage(
                    page_number=page_number + 1,
                    text=page.get_text()
                )
            )

        document.close()

        return pages
