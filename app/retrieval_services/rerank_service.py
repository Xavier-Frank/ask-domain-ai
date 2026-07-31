from sentence_transformers import CrossEncoder

from app.models.search.search_result import SearchResult


class RerankService:
    """
    Reranks semantic search results using a CrossEncoder.

    Unlike vector similarity, the CrossEncoder jointly evaluates the
    user's query and each retrieved chunk to produce a more accurate
    relevance score.
    """

    MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"

    _model: CrossEncoder | None = None

    @classmethod
    def _get_model(cls) -> CrossEncoder:
        """
        Lazily load the reranking model.
        """

        if cls._model is None:
            cls._model = CrossEncoder(cls.MODEL_NAME)

        return cls._model

    @classmethod
    def rerank(
        cls,
        question: str,
        results: list[SearchResult],
        top_k: int = 5
    ) -> list[SearchResult]:
        """
        Rerank retrieved chunks by semantic relevance.

        Args:
            question:
                User question.

            results:
                Chunks returned by Chroma.

            top_k:
                Number of chunks to return.

        Returns:
            Reranked search results.
        """

        if not results:
            return []

        model = cls._get_model()

        pairs = [
            (question, result.text)
            for result in results
        ]

        scores = model.predict(pairs)

        for result, score in zip(results, scores):
            result.rerank_score = float(score)

        results.sort(
            key=lambda r: r.rerank_score,
            reverse=True
        )

        return results[:2]