Ask Domain AI Backend
## Overview
Ask Domain AI is a modular Retrieval-Augmented Generation (RAG) backend built with FastAPI. It ingests PDF documents, indexes them into ChromaDB, retrieves relevant content using semantic search, reranks results, builds optimized prompts, and generates grounded answers with Ollama.

## Features
### API
- FastAPI
- Swagger/OpenAPI
- PDF upload
- Semantic search
- Streaming chat (SSE)

### Processing
- PDF extraction (PyMuPDF)
- Text cleaning
- Sentence-aware chunking
- Embeddings (all-MiniLM-L6-v2)
- ChromaDB indexing
- Cross-Encoder reranking
- Context & Prompt builders
- Ollama integration
## Architecture
```text
PDF Upload
    │
    ▼
Text Extraction
    │
    ▼
Cleaning
    │
    ▼
Sentence Chunking
    │
    ▼
Embeddings
    │
    ▼
ChromaDB
    │
    ▼
Semantic Search
    │
    ▼
Reranker
    │
    ▼
Context Builder
    │
    ▼
Prompt Builder
    │
    ▼
Ollama
    │
    ▼
Streaming Response (SSE)
```
## Tech Stack
| Component | Technology |
|---|---|
| Python | 3.12+ |
| Framework | FastAPI |
| Vector DB | ChromaDB |
| Embeddings | Sentence Transformers |
| LLM | Ollama (Qwen2.5:7B) |
| Streaming | SSE |
## Getting Started
```bash
python -m venv .venv
pip install -r requirements.txt

chroma run
ollama serve
ollama run qwen2.5:7b

uvicorn app.main:app --reload
```
## Endpoints
| Method | Endpoint |
|---|---|
| GET | /health |
| POST | /documents/upload |
| POST | /chat |
| POST | /chat/stream |
## Roadmap
- ✅ API Foundation
- ✅ Document Processing
- ✅ Semantic Search
- ✅ Retrieval Pipeline
- ✅ Ollama Integration
- 🚧 Next.js Frontend
- ⏳ Enterprise Features
