# Ask Domain AI

## Overview

Ask Domain AI is a Retrieval-Augmented Generation (RAG) application that enables users to ask natural language questions about domain-specific documents such as brochures, policy documents, user manuals, contracts, travel guides, and knowledge base articles.

Instead of relying solely on a large language model's general knowledge, the application retrieves relevant information from uploaded documents and uses an AI model to generate accurate, context-aware responses grounded in the document content.

The project is being developed incrementally, beginning with a robust document ingestion pipeline before introducing embeddings, vector search, and Large Language Model (LLM) integration.

The initial version focuses on PDF documents, with future support planned for additional document formats.

---

# Features

## Current

### API

* FastAPI backend
* Interactive Swagger/OpenAPI documentation
* Health check endpoint
* Document upload endpoint

### PDF Processing

* PDF upload
* Local document storage
* PDF text extraction using PyMuPDF
* Page-based document extraction
* Document metadata generation

### Text Processing

* Unicode normalization
* Control character removal
* Non-printable character removal
* Bullet removal
* Dot leader removal
* Standalone page number removal
* Whitespace normalization
* Hyphenated word repair

### Sentence Processing

* Sentence-aware parsing
* Page-aware sentence tracking

### Semantic Chunking

* Sentence-aware chunk generation
* Configurable chunk size
* Configurable sentence overlap
* Multi-page chunk support
* Chunk metadata generation
* Document processing pipeline

---

## Planned

* Automatic title extraction
* Section heading detection
* Chunk quality filtering
* Embedding generation
* Vector database integration
* Semantic search
* AI-powered question answering
* Multi-document knowledge base
* Conversation history
* Source citations
* Authentication and user management

---

# High-Level Architecture

```text
                ┌────────────────────┐
                │   PDF Document     │
                └─────────┬──────────┘
                          │
                          ▼
                Document Upload API
                          │
                          ▼
                  Save PDF to Disk
                          │
                          ▼
                  PDF Page Extraction
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
                  Document Processing
                          │
                          ▼
               Embedding Generation
                          │
                          ▼
                  Vector Database
                          ▲
                          │
                Semantic Search
                          ▲
                          │
                    User Question
                          │
                          ▼
                 Prompt Construction
                          │
                          ▼
               Large Language Model
                          │
                          ▼
              Natural Language Response
```

---

# Technology Stack

| Component         | Technology        |
| ----------------- | ----------------- |
| Language          | Python 3.12+      |
| Framework         | FastAPI           |
| API Server        | Uvicorn           |
| Data Validation   | Pydantic          |
| PDF Processing    | PyMuPDF           |
| API Documentation | Swagger / OpenAPI |

### Planned Technologies

* Sentence Transformers
* ChromaDB
* OpenAI Embeddings
* Ollama / OpenAI LLMs
* React (Frontend)

---

# Project Structure

```text
ask-domain-ai/
│
├── app/
│   ├── api/
│   │
│   ├── ingestion_services/
│   │   ├── chunk_service.py
│   │   ├── pdf_service.py
│   │   ├── sentence_service.py
│   │   └── text_cleaner.py
│   │
│   ├── models/
│   │   ├── document.py
│   │   ├── document_chunk.py
│   │   ├── document_page.py
│   │   ├── document_sentence.py
│   │   └── ...
│   │
│   ├── processors/
│   │   └── document_processor.py
│   │
│   ├── config.py
│   └── main.py
│
├── documents/
│   └── uploads/
│
├── requirements.txt
├── README.md
└── .venv/
```

---

# Getting Started

## Clone the repository

```bash
git clone <repository-url>
cd ask-domain-ai
```

## Create a virtual environment

```bash
python -m venv .venv
```

## Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Start the application

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://localhost:8000
```

---

# API Documentation

Once the application is running, the interactive API documentation can be accessed at:

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

---

# Available Endpoints

| Method | Endpoint            | Description                       |
| ------ | ------------------- | --------------------------------- |
| GET    | `/`                 | Application information           |
| GET    | `/health`           | Health check                      |
| POST   | `/documents/upload` | Upload and process a PDF document |

---

# Current Processing Pipeline

Each uploaded document passes through the following pipeline:

1. Upload PDF document.
2. Save the document locally.
3. Extract text from every page.
4. Clean extracted text.
5. Split text into sentences.
6. Generate overlapping semantic chunks.
7. Build a complete document model.
8. Return processed document metadata.

---

# Semantic Chunking Strategy

Ask Domain AI uses a sentence-aware chunking strategy designed for Retrieval-Augmented Generation.

Features include:

* Sentence boundaries are preserved.
* Chunks are generated using a configurable maximum size.
* Consecutive chunks overlap by configurable sentences to preserve context.
* Chunks may span multiple pages.
* Each chunk stores:

  * Document ID
  * Chunk ID
  * Start page
  * End page
  * Character count
  * Sentence count
  * Placeholder for embeddings

This provides significantly better retrieval quality than naive fixed-length chunking.

---

# Development Roadmap

## Phase 1 — API Foundation ✅

* [x] FastAPI project setup
* [x] Swagger documentation
* [x] Health endpoint
* [x] PDF upload
* [x] Local document storage

---

## Phase 2 — Document Ingestion ✅

* [x] PDF page extraction
* [x] Text cleaning
* [x] Sentence segmentation
* [x] Sentence-aware chunking
* [x] Multi-page chunk support
* [x] Document processing pipeline

---

## Phase 3 — Knowledge Base (In Progress)

* [ ] Document title extraction
* [ ] Section heading detection
* [ ] Chunk quality filtering
* [ ] Metadata enrichment

---

## Phase 4 — Semantic Search

* [ ] Generate embeddings
* [ ] Store embeddings in ChromaDB
* [ ] Similarity search

---

## Phase 5 — AI Chat

* [ ] Chat endpoint
* [ ] Prompt engineering
* [ ] Retrieval-Augmented Generation (RAG)
* [ ] Natural language response generation

---

## Phase 6 — Production Features

* [ ] Authentication
* [ ] Multiple knowledge bases
* [ ] Conversation history
* [ ] Source citations
* [ ] Docker support
* [ ] CI/CD pipeline

---

# Example Workflow

1. Upload a domain-specific PDF document.
2. Extract and clean the document text.
3. Split the text into meaningful sentences.
4. Build overlapping semantic chunks.
5. Generate embeddings for each chunk.
6. Store embeddings in a vector database.
7. Receive a user's question.
8. Retrieve the most relevant chunks.
9. Send the retrieved context to the language model.
10. Return a grounded natural language answer.

---

# Future Enhancements

Potential improvements include:

* Automatic title extraction
* Section heading detection
* OCR fallback for scanned PDFs
* Support for Microsoft Word, PowerPoint, and text documents
* Website crawling
* Hybrid keyword and semantic search
* Multi-language document support
* Administrative dashboard
* Analytics and usage metrics
* Feedback collection for answer quality

---

# License

This project is intended for educational and demonstration purposes. A production deployment should include proper security, authentication, monitoring, secret management, and scalable infrastructure.

---

# Author

**Xavier Oduor**

Ask Domain AI was created as a hands-on learning project to explore Retrieval-Augmented Generation (RAG), semantic search, document processing, vector databases, and Large Language Model integration. The project emphasizes building each component from first principles to gain a deep understanding of modern AI-powered knowledge systems.
