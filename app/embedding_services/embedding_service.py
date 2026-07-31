from sentence_transformers import SentenceTransformer

from app.models.ingestion.document_chunk import DocumentChunk


class EmbeddingService:
    """
    Generates semantic vector embeddings for document chunks.

    The underlying embedding model is loaded only once and reused
    across the application's lifetime to improve performance.
    """

    MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

    _model: SentenceTransformer | None = None

    @classmethod
    def _get_model(cls) -> SentenceTransformer:
        """
        Lazily load the embedding model.

        Returns:
            Loaded SentenceTransformer model.
        """
        if cls._model is None:
            cls._model = SentenceTransformer(cls.MODEL_NAME)

        return cls._model

    def embed_chunk(
        self,
        chunk: DocumentChunk
    ) -> DocumentChunk:
        """
        Generate an embedding for a single document chunk.

        Args:
            chunk: Document chunk.

        Returns:
            Updated DocumentChunk containing the embedding.
        """

        model = self._get_model()

        embedding = model.encode(
            chunk.text,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        chunk.embedding = embedding.tolist()

        return chunk

    def embed_chunks(
        self,
        chunks: list[DocumentChunk]
    ) -> list[DocumentChunk]:
        """
        Generate embeddings for multiple chunks in a single batch.
        Args:
            chunks: List of document chunks.

        Returns:
            Updated list of chunks containing embeddings.
        """

        if not chunks:
            return []

        model = self._get_model()

        texts = [
            chunk.text
            for chunk in chunks
        ]

        embeddings = model.encode(
            texts,
            batch_size=32,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=False
        )

        for chunk, embedding in zip(chunks, embeddings):
            chunk.embedding = embedding.tolist()

        return chunks

    def embed_query(
        self,
        query: str
    ) -> list[float]:
        """
        Generate an embedding for a user's search query.

        Args:
            query: User question.

        Returns:
            Query embedding as a list of floats.
        """

        model = self._get_model()

        embedding = model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embedding.tolist()

    @classmethod
    def embedding_dimension(cls) -> int:
        """
        Return the dimensionality of the embedding vectors.

        Raises:
            ValueError: If the model does not expose an embedding dimension.
        """

        model = cls._get_model()

        dimension = model.get_embedding_dimension()

        if dimension is None:
            raise ValueError(
                "Unable to determine embedding dimension."
            )

        return dimension