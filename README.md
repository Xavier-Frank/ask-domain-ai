# Ask Domain AI

## Overview

Ask Domain AI is a Retrieval-Augmented Generation (RAG) application that enables users to ask natural language questions about domain-specific documents such as brochures, policy documents, user manuals, contracts, and knowledge base articles.

Instead of relying solely on a large language model's general knowledge, the application retrieves relevant information from uploaded documents and uses an AI model to generate accurate, context-aware responses.

The initial version focuses on PDF documents, with future support planned for additional document formats.

---

## Features

### Current

* FastAPI backend
* Interactive Swagger/OpenAPI documentation
* Health check endpoint
* PDF document upload
* PDF text extraction using PyMuPDF

### Planned

* Document chunking
* Embedding generation
* Vector database integration
* Semantic search
* AI-powered question answering
* Multi-document knowledge base
* Conversation history
* Source citations
* Authentication and user management

---

## High-Level Architecture

```text
                ┌────────────────────┐
                │   PDF Document     │
                └─────────┬──────────┘
                          │
                          ▼
                Document Upload API
                          │
                          ▼
                  PDF Text Extraction
                          │
                          ▼
                    Text Chunking
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

## Technology Stack

| Component         | Technology        |
| ----------------- | ----------------- |
| Language          | Python 3.x        |
| Framework         | FastAPI           |
| API Server        | Uvicorn           |
| PDF Processing    | PyMuPDF           |
| API Documentation | Swagger / OpenAPI |

### Planned Technologies

* ChromaDB
* OpenAI Embeddings
* GPT Models
* Sentence Transformers
* React (Frontend)

---

## Project Structure

```text
ask-domain-ai/
│
├── app/
│   ├── api/
│   ├── services/
│   ├── models/
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

## Getting Started

### Clone the repository

```bash
git clone <repository-url>
cd ask-domain-ai
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the application

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```
http://localhost:8000
```

---

## API Documentation

Once the application is running, the interactive API documentation can be accessed at:

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

## Available Endpoints

| Method | Endpoint            | Description             |
| ------ | ------------------- | ----------------------- |
| GET    | `/`                 | Application information |
| GET    | `/health`           | Health check            |
| POST   | `/documents/upload` | Upload a PDF document   |

---

## Development Roadmap

### Phase 1 — API Foundation

* [x] FastAPI project setup
* [x] Swagger documentation
* [x] Health endpoint
* [x] PDF upload
* [x] PDF text extraction

### Phase 2 — Knowledge Base

* [ ] Text chunking
* [ ] Metadata extraction
* [ ] Document indexing

### Phase 3 — Semantic Search

* [ ] Generate embeddings
* [ ] Store embeddings in ChromaDB
* [ ] Similarity search

### Phase 4 — AI Chat

* [ ] Chat endpoint
* [ ] Prompt engineering
* [ ] Response generation

### Phase 5 — Production Features

* [ ] Authentication
* [ ] Multiple knowledge bases
* [ ] Conversation history
* [ ] Source citations
* [ ] Docker support
* [ ] CI/CD pipeline

---

## Example Workflow

1. Upload a domain-specific PDF document.
2. Extract the document's text.
3. Split the document into searchable chunks.
4. Generate embeddings for each chunk.
5. Store the embeddings in a vector database.
6. Receive a user's question.
7. Retrieve the most relevant chunks.
8. Send the retrieved context to the language model.
9. Return a natural language answer grounded in the document.

---

## Future Enhancements

Potential improvements include:

* Support for Microsoft Word and PowerPoint documents
* Website crawling
* OCR support for scanned PDFs
* Hybrid keyword and semantic search
* Multi-language document support
* Administrative dashboard
* Analytics and usage metrics
* Feedback collection for answer quality

---

## License

This project is intended for educational and demonstration purposes. A production deployment should include proper security, authentication, monitoring, and secret management.

---

## Author

**Xavier Oduor**

Ask Domain AI was created as a learning project to explore Retrieval-Augmented Generation (RAG), vector databases, semantic search, and large language model integration for domain-specific question answering.
