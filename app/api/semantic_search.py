from fastapi import APIRouter

from app.models.search.search_request import SearchRequest
from app.retrieval_services.search_service import SearchService

router = APIRouter(prefix="/search", tags=["Search"])

@router.post("/user-query", tags=["Search"])
def search(request: SearchRequest):
    return SearchService.search(request)