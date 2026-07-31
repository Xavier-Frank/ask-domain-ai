from fastapi import FastAPI
from app.api.documents import router as document_router
from app.api.semantic_search import router as search_router
from app.api.ai_search import router as ai_search
from app.vector_store.chroma_service import ChromaService
from app.vector_store.collection_service import CollectionService

app = FastAPI(
    title="Ask Domain AI",
    description="Domain Specific AI Assistant",
    version="1.0",
)

app.include_router(document_router)
app.include_router(search_router)

app.include_router(ai_search)

@app.get("/")
def home():
    return {
        "application" : "Ask Domain AI",
        "version" : "1.0",
        "status" : "up & running",
    }

@app.get("/health")
def health():
    client = ChromaService.get_client()
    heartbeat = client.heartbeat()
    return {
        "status" : "up and running",
        "chroma_db_heartbeat": heartbeat
    }

@app.get("/collections")
def collections():

    collection = CollectionService.get_collections()

    result = collection.peek()

    return {
        "ids": result["ids"],
        "documents": result["documents"],
        "metadatas": result["metadatas"]
    }