# Ask Domain AI Backend

## Overview

Ask Domain AI is a modular Retrieval-Augmented Generation (RAG) backend built with FastAPI. It ingests PDF documents into a knowledge base, performs semantic retrieval with ChromaDB, reranks results for relevance, constructs optimized prompts, and streams grounded responses from Ollama using Server-Sent Events (SSE).

---

## Features

### API
- FastAPI
- Swagger / OpenAPI
- PDF upload & indexing
- Semantic document search
- Streaming chat (SSE)
- Health check endpoint

### RAG Pipeline
- PDF extraction (PyMuPDF)
- Text cleaning & normalization
- Sentence-aware chunking
- Embedding generation
- ChromaDB vector storage
- Semantic retrieval
- Cross-Encoder reranking
- Context construction
- Prompt generation
- Ollama (Qwen2.5) integration
- Streaming token generation

### Performance
- Lazy-loaded AI models
- Model warm-up during application startup
- Cached embedding & reranking models
- Streaming responses with low first-token latency

---

## Architecture

```text
                PDF Upload
                     │
                     ▼
            PDF Text Extraction
                     │
                     ▼
          Text Cleaning & Normalization
                     │
                     ▼
          Sentence-aware Chunking
                     │
                     ▼
          Embedding Generation
                     │
                     ▼
             ChromaDB Indexing
                     │
                     ▼
──────────────────────────────────────────

              User Question
                     │
                     ▼
          Query Embedding
                     │
                     ▼
          Semantic Retrieval
                     │
                     ▼
          Cross-Encoder Reranking
                     │
                     ▼
            Context Builder
                     │
                     ▼
            Prompt Builder
                     │
                     ▼
           Ollama (Qwen2.5)
                     │
                     ▼
        Streaming Response (SSE)
```

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.12+ |
| Framework | FastAPI |
| Vector Database | ChromaDB |
| PDF Processing | PyMuPDF |
| Embeddings | all-MiniLM-L6-v2 |
| Reranker | CrossEncoder (Sentence Transformers) |
| LLM | Ollama (Qwen2.5:7B) |
| Streaming | Server-Sent Events (SSE) |

---

## Getting Started

```bash
# Create virtual environment
python -m venv .venv

# Install dependencies
pip install -r requirements.txt

# Start ChromaDB
chroma run

# Start Ollama
ollama serve

# Download the model
ollama pull qwen2.5:7b

# Run the API
uvicorn app.main:app --reload
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/api/v1/documents/upload` | Upload and index PDF documents |
| POST | `/api/v1/chat` | Generate a complete response |
| POST | `/api/v1/chat/stream` | Stream AI responses via SSE |

---

## Request Flow

```text
User
   │
   ▼
FastAPI
   │
   ▼
Search Service
   │
   ├── Query Embedding
   ├── ChromaDB Retrieval
   ├── Cross-Encoder Reranking
   └── Prompt Builder
   │
   ▼
Ollama
   │
   ▼
Server-Sent Events
   │
   ▼
Frontend
```

---

## Roadmap

- ✅ PDF ingestion
- ✅ Text preprocessing
- ✅ Semantic search
- ✅ Cross-Encoder reranking
- ✅ Prompt engineering
- ✅ ChromaDB integration
- ✅ Ollama integration
- ✅ Streaming chat (SSE)
- ✅ Model warm-up
- ✅ Next.js frontend
- ⏳ Conversation history
- ⏳ Multi-document collections
- ⏳ Hybrid search (Keyword + Vector)
- ⏳ Authentication & user management