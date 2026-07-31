from fastapi import APIRouter

from app.llm_services.ollama_service import OllamaService
from app.models.search.search_request import SearchRequest

router = APIRouter(prefix="/search", tags=["Search"])

@router.post("/ai-query", tags=["Search"])
def search(request: SearchRequest):
    return OllamaService.generate(request)