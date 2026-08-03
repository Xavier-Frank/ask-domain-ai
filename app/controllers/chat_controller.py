from fastapi import APIRouter

from app.models.search.search_request import SearchRequest
from app.services.llm_services.llm_service import LLMService
from app.services.retrieval_services.search_service import SearchService

router = APIRouter(prefix="/controllers/v1", tags=["Search"])

@router.post("/generate-prompt", tags=["Search"])
def search(request: SearchRequest):
    return SearchService.search(request)

@router.post("/chat", tags=["Search"])
def search(request: SearchRequest):

    prompt_req = SearchService.search(request)

    answer = LLMService.generate(prompt_req)

    return answer
