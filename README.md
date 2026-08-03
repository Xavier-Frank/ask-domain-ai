Ask Domain AI

A Retrieval-Augmented Generation (RAG) backend for querying domain-specific documents using semantic search and local LLMs.

Ask Domain AI ingests PDF documents, converts them into semantic embeddings, stores them in ChromaDB, retrieves relevant content using vector search, reranks the results, and generates grounded answers using Ollama.

✨ Features
📄 Document Processing
PDF upload
PyMuPDF text extraction
Text cleaning & normalization
Sentence-aware parsing
Semantic chunking
🧠 Retrieval
Sentence Transformer embeddings
ChromaDB vector storage
Semantic similarity search
Cross-Encoder reranking
Context construction
🤖 AI
Ollama integration
Prompt generation
Streaming responses (SSE)
Source attribution
Token usage tracking
🚀 API
FastAPI
Swagger / OpenAPI
Health endpoint
Document upload
Chat endpoint
Streaming chat endpoint
🏗 Architecture
                PDF Upload
                     │
                     ▼
            Text Extraction
                     │
                     ▼
             Text Cleaning
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
                ChromaDB
                     ▲
                     │
          Semantic Retrieval
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
              Ollama (LLM)
                     │
                     ▼
          Streaming Response
⚙️ Technology Stack
Component	Technology
Language	Python 3.12+
Framework	FastAPI
PDF Processing	PyMuPDF
Embeddings	Sentence Transformers
Vector Database	ChromaDB
Reranker	Cross Encoder
LLM	Ollama
Default Model	Qwen2.5 7B
HTTP Client	HTTPX
Streaming	Server-Sent Events (SSE)
📂 Project Structure
ask-domain-ai/
│
├── app/
│   ├── api/
│   ├── configs/
│   ├── ingestion_services/
│   ├── embedding_services/
│   ├── retrieval_services/
│   ├── llm_services/
│   ├── vector_store/
│   ├── processors/
│   ├── models/
│   └── main.py
│
├── documents/
│   └── uploads/
│
├── requirements.txt
└── README.md
🚀 Getting Started
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

Pull and run a model:

ollama run qwen2.5:7b
Start FastAPI
uvicorn app.main:app --reload
📚 API Documentation
Interface	URL
Swagger	http://localhost:8000/docs
ReDoc	http://localhost:8000/redoc

🔄 Processing Pipeline

PDF
 │
 ▼
Extract Text
 │
 ▼
Clean Text
 │
 ▼
Sentence Parsing
 │
 ▼
Semantic Chunking
 │
 ▼
Embeddings
 │
 ▼
ChromaDB
 │
 ▼
Similarity Search
 │
 ▼
Reranking
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
🌐 API Endpoints
Method	Endpoint	Description
GET	/	API information
GET	/health	Health check
POST	/documents/upload	Upload & index PDF
POST	/chat	Ask questions
POST	/chat/stream	Streaming chat (SSE)
🛣 Roadmap
✅ Phase 1 — Foundation
 FastAPI
 Swagger
 PDF Upload
✅ Phase 2 — Document Processing
 PDF extraction
 Text cleaning
 Sentence segmentation
 Semantic chunking
✅ Phase 3 — Semantic Search
 Sentence embeddings
 ChromaDB
 Similarity search
✅ Phase 4 — Retrieval
 Cross-Encoder reranking
 Context builder
 Prompt builder
✅ Phase 5 — AI
 Ollama integration
 Streaming responses
 Source attribution
🚧 Phase 6 — Frontend
 Next.js chatbot
 Floating assistant
 Markdown rendering
 Source citation cards
📌 Future
 Document title extraction
 OCR support
 Word & PowerPoint support
 Multi-document collections
 Authentication
 Conversation history
 Docker & Kubernetes
 CI/CD
📈 RAG Workflow
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Chunk Document
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
──────────────────────────────
      │
User Question
      │
      ▼
Embed Query
      │
      ▼
Similarity Search
      │
      ▼
Rerank Results
      │
      ▼
Build Context
      │
      ▼
Generate Prompt
      │
      ▼
Ollama
      │
      ▼
Answer + Sources
🔮 Future Vision

Ask Domain AI is evolving into a modular enterprise RAG platform with support for:

Multiple document formats
OCR for scanned documents
Hybrid keyword + semantic search
Multi-language support
Multiple knowledge bases
Conversation memory
Analytics dashboard
Cloud-native deployment
📄 License

This project is intended for educational and research purposes. Production deployments should include authentication, monitoring, observability, and secure secret management.

👨‍💻 Author

Xavier Oduor

Ask Domain AI is a hands-on project built to explore the complete RAG lifecycle—from document ingestion and semantic indexing to retrieval, reranking, prompt engineering, and local LLM inference with Ollama.