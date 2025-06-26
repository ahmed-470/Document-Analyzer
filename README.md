# RAG Document Analyzer (Streamlit + OpenAI)

## Overview
This application is a Retrieval-Augmented Generation (RAG) prototype that allows users to:
- Upload or paste plain text documents
- Ask natural language questions
- Get generated responses based on document context

Built with Streamlit for UI, OpenAI APIs for LLM and embeddings, and a modular architecture.

---

## Features
- Text document upload and QA
- RAG pipeline (embed → retrieve → generate)
- Session-based chat history
- Streaming UI via Streamlit
- Works in-browser with minimal setup

---


## Run the App via Docker

```bash
# Build the image
docker build -t rag-app .

# Run the container (app available at http://localhost:8080)
docker run -p 8080:8080 rag-app
```
Then visit `http://localhost:8080`

## Run Tests (Docker)
```bash
docker run rag-app python /home/src/tests/run_tests.py
```

---

## File Structure
```
/home
├── app.py                # Streamlit entrypoint
├── main.py               # (Optional: graph/logic entry)
├── requirements.txt
├── Dockerfile
└── src/
    ├── ui/               # Streamlit interface
    ├── llm/              # OpenAI LLM interface
    ├── graph/            # RAG pipeline orchestration
    ├── nodes/            # Model + RAG nodes
    ├── tools/            # Embedding, retrieval, dataset utils
    ├── state/            # Session state for Streamlit
    ├── tests/            # Unit/integration tests
    └── README.md         # This file
```

---

## Notes
- Set your OpenAI API key in the UI when prompted.
- Retrieval uses OpenAI embeddings + cosine similarity (via sklearn).
- `ccdv/arxiv-summarization` used for dev/test purposes.

---

## Authors & Licensing
This is a prototype for evaluation purposes. Modify and extend as needed.