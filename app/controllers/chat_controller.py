from asyncio import log

from fastapi import APIRouter
from starlette.responses import StreamingResponse

from app.models.prompt.prompt_request import PromptRequest
from app.models.search.search_request import SearchRequest
from app.services.llm_services.llm_service import LLMService
from app.services.llm_services.prompt_builder_service import PromptBuilderService
from app.services.retrieval_services.intent_service import IntentService
from app.services.retrieval_services.search_service import SearchService

router = APIRouter(prefix="/api/v1", tags=["Search"])

@router.post("/generate-prompt", tags=["Search"])
def search(request: SearchRequest):
    if IntentService.requires_search(request.question):
        print("Requires search...")
        return SearchService.search(request)
    else:
        print("Does not require search...")
        prompt = PromptBuilderService.build_greeting_prompt(request.question)
        return PromptRequest(question=request.question, prompt=prompt, sources=[])


@router.post("/chat", tags=["Search"])
def search(request: SearchRequest):

    if IntentService.requires_search(request.question):

        prompt_req = SearchService.search(request)

    else:

        prompt = PromptBuilderService.build_greeting_prompt(request.question)

        prompt_req = PromptRequest(question=request.question, prompt=prompt, sources=[])

    answer = LLMService.generate(prompt_req)

    return answer

@router.post("/chat/stream", tags=["Search"])
def stream_chat(request: SearchRequest):
    if IntentService.requires_search(request.question):

        prompt = SearchService.search(request)

    else:

        prompt_req = PromptBuilderService.build_greeting_prompt(request.question)

        prompt = PromptRequest(question=request.question, prompt=prompt_req, sources=[])

    return StreamingResponse(
        LLMService.generate_stream(prompt),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )