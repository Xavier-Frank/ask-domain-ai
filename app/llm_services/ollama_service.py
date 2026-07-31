from app.retrieval_services.search_service import SearchService


class OllamaService:

    @classmethod
    def search(cls, request):

        "Generate prompt"
        search_result = SearchService.search(request=request)

        ai_prompt = search_result.prompt

        return ai_prompt
