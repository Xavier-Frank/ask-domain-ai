from fastapi import FastAPI
from app.api.documents import router as document_router

app = FastAPI(
    title="Ask Domain AI",
    description="Domain Specific AI Assistant",
    version="1.0",
)

app.include_router(document_router)

@app.get("/")
def home():
    return {
        "application" : "Ask Domain AI",
        "version" : "1.0",
        "status" : "up & running",
    }

@app.get("/health")
def health():
    return {
        "status" : "up and running",
    }