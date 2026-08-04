from pathlib import Path

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.controllers.documents_controller import router as document_router
from app.controllers.chat_controller import router as search_router
from app.vector_store.chroma_service import ChromaService
from app.vector_store.collection_service import CollectionService

app = FastAPI(
    title="Ask Domain AI",
    description="Domain Specific AI Assistant",
    version="1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


app.include_router(document_router)
app.include_router(search_router)
@app.get("/")
def home():
    dir_curr = Path(__file__).resolve().parent.parent
    doc = dir_curr / "app/documents"
    return {
        "application" : "Ask Domain AI",
        "version" : "1.0",
        "status" : "up & running",
        "Base Url" : dir_curr,
        "Docs" : doc
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