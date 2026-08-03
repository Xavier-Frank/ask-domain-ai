import chromadb

from app.configs.config import CHROMA_DB_DIR


class ChromaService:

    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = chromadb.PersistentClient(
                path=str(CHROMA_DB_DIR)
            )

        return cls._client