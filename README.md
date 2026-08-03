Ask Domain AI Backend
Overview

Ask Domain AI is a Retrieval-Augmented Generation (RAG) backend built with FastAPI that enables users to ask natural language questions about domain-specific documents such as travel guides, policies, manuals, contracts, knowledge bases, and technical documentation.

Unlike traditional chatbots that rely solely on an LLM's general knowledge, Ask Domain AI grounds every response in uploaded documents. It extracts document content, transforms it into semantic embeddings, stores the vectors in ChromaDB, retrieves the most relevant information using semantic search, reranks the results for higher accuracy, constructs an optimized prompt, and generates grounded answers using a locally hosted Ollama Large Language Model.

The project is designed as a modular RAG framework where each stage of the pipeline is independently extensible.

Features
API
FastAPI backend
Interactive Swagger/OpenAPI documentation
Health check endpoint
Document upload endpoint
Semantic search endpoint
Streaming chat endpoint (SSE)
Document Ingestion
PDF upload
Local document storage
PDF text extraction using PyMuPDF
Page-aware document parsing
Metadata extraction
Processing time tracking
Text Processing
Unicode normalization
Removal of control characters
Removal of non-printable characters
Bullet cleanup
Dot leader cleanup
Page number removal
Whitespace normalization
Hyphenated word reconstruction
Sentence Processing
Sentence-aware parsing
Page-aware sentence tracking
Sentence metadata generation
Semantic Chunking
Sentence-aware chunk generation
Configurable chunk size
Configurable sentence overlap
Multi-page chunk support
Chunk metadata
Character statistics
Sentence statistics
Embeddings
Sentence Transformers integration
all-MiniLM-L6-v2 embedding model
Batch embedding generation
Query embedding generation
Normalized embeddings
Vector Database
ChromaDB integration
Automatic collection creation
Document indexing
Vector persistence
Similarity search
Metadata filtering support
Retrieval
Semantic vector search
Cross-Encoder reranking
Context construction
Prompt generation
Source attribution
AI
Ollama integration
Local LLM inference
Streaming responses
Server-Sent Events (SSE)
Prompt token tracking
Completion token tracking
High-Level Architecture
                     PDF Document
                           │
                           ▼
                  Document Upload API
                           │
                           ▼
                  Local Document Storage
                           │
                           ▼
                 PDF Text Extraction
                           │
                           ▼
                     Text Cleaning
                           │
                           ▼
                 Sentence Segmentation
                           │
                           ▼
               Semantic Chunk Generation
                           │
                           ▼
                 Embedding Generation
                           │
                           ▼
                     ChromaDB
                           ▲
                           │
                Semantic Similarity Search
                           │
                           ▼
                 Cross-Encoder Reranker
                           │
                           ▼
                  Context Builder
                           │
                           ▼
                  Prompt Builder
                           │
                           ▼
                     Ollama LLM
                           │
                           ▼
              Streaming AI Response (SSE)
Technology Stack
Component	Technology
Language	Python 3.12+
Framework	FastAPI
Validation	Pydantic
API Server	Uvicorn
PDF Processing	PyMuPDF
Embeddings	Sentence Transformers
Embedding Model	all-MiniLM-L6-v2
Reranker	ms-marco-MiniLM-L-6-v2
Vector Database	ChromaDB
LLM	Ollama
Default Model	Qwen2.5 7B
HTTP Client	HTTPX
Streaming	Server-Sent Events (SSE)
Project Structure
ask-domain-ai/

app/
│
├── api/
│
├── configs/
│
├── embedding_services/
│   └── embedding_service.py
│
├── ingestion_services/
│   ├── pdf_service.py
│   ├── sentence_service.py
│   ├── chunk_service.py
│   └── text_cleaner.py
│
├── llm_services/
│   ├── context_builder.py
│   ├── prompt_builder_service.py
│   └── ollama_service.py
│
├── retrieval_services/
│   ├── search_service.py
│   └── rerank_service.py
│
├── vector_store/
│   ├── collection_service.py
│   └── vector_store_service.py
│
├── models/
│
├── processors/
│
└── main.py

documents/
└── uploads/

README.md
requirements.txt
Getting Started
Clone
git clone <repository-url>

cd ask-domain-ai
Create Virtual Environment
python -m venv .venv

Windows

.venv\Scripts\activate

Linux/macOS

source .venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Start ChromaDB
chroma run
Start Ollama
ollama serve

Run your preferred model:

ollama run qwen2.5:7b
Start FastAPI
uvicorn app.main:app --reload
API Documentation

Swagger

http://localhost:8000/docs

ReDoc

http://localhost:8000/redoc
Current Processing Pipeline

Every uploaded document passes through the following stages:

Upload PDF
Save document locally
Extract page text
Clean text
Parse sentences
Generate semantic chunks
Generate embeddings
Store vectors in ChromaDB
Receive user question
Embed question
Semantic similarity search
Cross-Encoder reranking
Build retrieval context
Construct LLM prompt
Generate answer using Ollama
Stream answer to the client with source citations
Available Endpoints
Method	Endpoint	Description
GET	/	API information
GET	/health	Health check
POST	/documents/upload	Upload and index document
POST	/chat	AI question answering
POST	/chat/stream	Streaming AI responses
Development Roadmap
Phase 1 — API Foundation ✅
 FastAPI setup
 Swagger
 Health endpoint
 PDF upload
Phase 2 — Document Processing ✅
 PDF extraction
 Text cleaning
 Sentence segmentation
 Semantic chunking
 Multi-page chunks
Phase 3 — Semantic Search ✅
 Sentence Transformer embeddings
 Batch embedding generation
 ChromaDB integration
 Vector indexing
 Semantic similarity search
Phase 4 — Retrieval Enhancement ✅
 Cross-Encoder reranking
 Context builder
 Prompt builder
 Source attribution
Phase 5 — AI Generation ✅
 Ollama integration
 Local LLM inference
 Streaming responses (SSE)
 Token usage tracking
 Prompt generation
Phase 6 — Frontend (In Progress)
 Next.js chatbot
 Floating AI assistant
 Streaming UI
 Markdown rendering
 Source citation cards
Phase 7 — Future Enhancements
 Automatic document title extraction
 Section heading extraction
 OCR support
 Microsoft Word support
 PowerPoint support
 Multi-document collections
 Conversation history
 Authentication
 Docker deployment
 Kubernetes deployment
 CI/CD pipeline
Example RAG Workflow
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Clean Text
      │
      ▼
Sentence Segmentation
      │
      ▼
Semantic Chunking
      │
      ▼
Embedding Generation
      │
      ▼
ChromaDB Index
      │
────────────────────────────────────────────
      │
User Question
      │
      ▼
Question Embedding
      │
      ▼
Similarity Search
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
Ollama
      │
      ▼
Streaming Answer
Future Vision

The long-term vision for Ask Domain AI is to evolve into a complete enterprise knowledge assistant capable of:

Supporting multiple document formats (PDF, Word, PowerPoint, HTML)
Managing multiple knowledge bases
Integrating hybrid keyword and semantic retrieval
Performing OCR on scanned documents
Providing multilingual document search
Delivering conversational memory
Offering authentication and role-based access
Exposing analytics and document usage insights
Deploying as a scalable cloud-native RAG platform
License

This project is intended for educational, research, and demonstration purposes. A production deployment should include authentication, authorization, monitoring, secret management, observability, and scalable infrastructure.

Author

Xavier Oduor

Ask Domain AI is a hands-on engineering project built to explore the complete Retrieval-Augmented Generation (RAG) lifecycle—from document ingestion and semantic indexing to vector retrieval, reranking, prompt engineering, and local Large Language Model integration using Ollama. The project emphasizes understanding and implementing every layer of a modern AI-powered knowledge system from first principles.