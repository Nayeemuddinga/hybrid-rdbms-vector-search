import uuid, json
from sqlalchemy import text
from config.db import engine
from embeddings.embedding_utils import generate_embedding

docs = json.load(open("data/sample_docs.json"))

with engine.begin() as conn:
    for d in docs:
        doc_id = uuid.uuid4()
        conn.execute(text("""
            INSERT INTO documents VALUES (:id,:t,:c,now())
        """), {"id": doc_id, "t": d["title"], "c": d["content"]})

        emb = generate_embedding(d["content"])
        conn.execute(text("""
            INSERT INTO document_embeddings
            VALUES (:id,:e,'v1',now())
        """), {"id": doc_id, "e": emb})
