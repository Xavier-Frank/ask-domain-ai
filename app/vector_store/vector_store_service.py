"""
this service is responsible for adding vectors, updating vectors, deleting vectors, and similarity search
"""
from app.models.ingestion.document_models import Document
from app.vector_store.collection_service import CollectionService


class VectorStoreService:
    """
    Handle indexing and retrieval of document embeddings
    """

    @staticmethod
    def index_document(
            document: Document,
    ):
        """
        Store every chunk inside chromadb
        :param document: document chunks
        :return:
        """

        collection = CollectionService.get_collections()

        ids = []
        embeddings = []
        documents = []
        metadata = []

        for chunk in document.chunks:

            ids.append(
                f"{document.id}_{chunk.chunk_id}"
            )

            embeddings.append(
                chunk.embedding
            )

            documents.append(
                chunk.text
            )

            metadata.append(
                {
                    "document_id": document.id,
                    "filename": document.filename,
                    "chunk_id": chunk.chunk_id,
                    "uploaded_at": document.uploaded_at.isoformat(),
                    "processing_time": document.processing_time,
                    "start_page": chunk.start_page,
                    "end_page": chunk.end_page,
                    "character_count": chunk.character_count,
                    "sentence_count": chunk.sentence_count
                }
            )

        collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadata,
        )