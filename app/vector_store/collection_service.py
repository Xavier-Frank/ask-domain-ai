"""
    this service is responsible for creating collections, deleting collections
    , and retrieving collections
"""
from chromadb.api.models.Collection import Collection

from app.vector_store.chroma_service import ChromaService


class CollectionService:
    """
    Manages ChromaBD collections
    """

    COLLECTION_NAME = "ask-domain-ai"

    _collection: Collection | None = None

    @classmethod
    def get_collections(cls) -> Collection:
        if cls._collection is None:
            client = ChromaService.get_client()
            cls._collection = client.get_or_create_collection(
                name=cls.COLLECTION_NAME,
                metadata={
                    "description": "Knowledge base for Ask Domain AI"
                }
            )

        return cls._collection

    @classmethod
    def delete_collection(cls):
        """
        Deletes collection
        :return: void
        """
        client = ChromaService.get_client()
        client.delete_collection(
            cls.COLLECTION_NAME
        )

    @classmethod
    def list_collections(cls):
        client = ChromaService.get_client()

        return client.list_collections()
