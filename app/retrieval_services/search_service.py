from app.embedding_services.embedding_service import EmbeddingService
from app.models.search.search_request import SearchRequest
from app.models.search.search_result import SearchResult
from app.retrieval_services.rerank_service import RerankService
from app.vector_store.collection_service import CollectionService


class SearchService:
    """
    Performs semantic similarity searches against ChromaDB.
    """

    @staticmethod
    def search(
        request: SearchRequest
    ) -> list[SearchResult]:

        collection = CollectionService.get_collections()

        query_embedding = EmbeddingService.embed_query(
            request.question
        )

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=request.top_k,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

        search_results = []

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances
        ):

            search_results.append(

                SearchResult(
                    chunk_id=metadata["chunk_id"],
                    filename=metadata["filename"],
                    start_page=metadata["start_page"],
                    end_page=metadata["end_page"],
                    text=document,
                    similarity=distance
                )

            )

        search_results = RerankService.rerank(
            question=request.question,
            results=search_results,
            top_k=request.top_k
        )

        return search_results