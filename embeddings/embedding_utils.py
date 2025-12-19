import uuid, json
from sqlalchemy import text
from config.db_config import engine
from embeddings.embedding_utils import generate_embedding

with open("data/sample_documents.json") as f:
    docs = json.load(f)

with engine.begin() as conn:
    for d in docs:
        doc_id = uuid.uuid4()
        conn.execute(text("""
            INSERT INTO documents (doc_id, title, content)
            VALUES (:id, :title, :content)
        """), {"id": doc_id, "title": d["title"], "content": d["content"]})

        embedding = generate_embedding(d["content"])

        conn.execute(text("""
            INSERT INTO document_embeddings
            (doc_id, embedding, embedding_version)
            VALUES (:id, :embedding, 'v1')
        """), {"id": doc_id, "embedding": embedding})

