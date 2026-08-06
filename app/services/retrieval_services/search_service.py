from app.models.context.RetrievalContext import RetrievalContext
from app.models.prompt.prompt_request import PromptRequest
from app.models.search.search_request import SearchRequest
from app.models.search.search_result import SearchResult
from app.services.embedding_services.embedding_service import EmbeddingService
from app.services.llm_services.context_builder import ContextBuilder
from app.services.llm_services.prompt_builder_service import PromptBuilderService
from app.services.retrieval_services.rerank_service import RerankService
from app.vector_store.collection_service import CollectionService


class SearchService:
    """
    Executes the complete retrieval pipeline.

    Pipeline:
        1. Embed user query
        2. Search ChromaDB
        3. Map search results
        4. Rerank retrieved chunks
        5. Build retrieval context
        6. Build LLM prompt
    """

    @classmethod
    def search(
        cls,
        request: SearchRequest
    ) -> PromptRequest:

        query_embedding = EmbeddingService.embed_query(
            request.question
        )

        collection = CollectionService.get_collections()

        response = collection.query(
            query_embeddings=[query_embedding],
            n_results=request.top_k,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

        search_results = cls._map_search_results(response)

        reranked_results = RerankService.rerank(
            question=request.question,
            results=search_results,
            top_k=request.top_k
        )

        retrieval_context = RetrievalContext(
            question=request.question,
            context=ContextBuilder.build(reranked_results),
            sources=reranked_results
        )

        prompt = PromptBuilderService.build(
            retrieval_context
        )

        return PromptRequest(
            question=request.question,
            prompt=prompt,
            sources=reranked_results
        )

    @staticmethod
    def _map_search_results(
        response: dict
    ) -> list[SearchResult]:
        """
        Convert the raw ChromaDB response into SearchResult objects.
        """

        documents = response["documents"][0]
        metadatas = response["metadatas"][0]
        distances = response["distances"][0]

        results: list[SearchResult] = []

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances
        ):

            results.append(
                SearchResult(
                    chunk_id=metadata["chunk_id"],
                    filename=metadata["filename"],
                    start_page=metadata["start_page"],
                    end_page=metadata["end_page"],
                    text=document,
                    similarity=distance
                )
            )

        return results