# Hybrid RDBMS + Vector Search Platform

This project demonstrates a production-ready hybrid search platform
using PostgreSQL, pgvector, and Python.

## Features
- Semantic search with pgvector
- Hybrid keyword + vector querying
- Embedding versioning
- Dockerized deployment
- Governance & auditability

## Run
1. docker compose up -d
2. Execute SQL files in /database
3. pip install -r requirements.txt
4. python embeddings/embed_documents.py
5. python search/semantic_search.py

