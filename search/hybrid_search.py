from sqlalchemy import text
from config.db_config import engine
from embeddings.embedding_utils import generate_embedding

query = "database failover strategy"
vector = generate_embedding(query)

with engine.connect() as conn:
    result = conn.execute(text("""
        SELECT d.title, d.content
        FROM documents d
        JOIN document_embeddings e ON d.doc_id = e.doc_id
        ORDER BY e.embedding <=> :vector
        LIMIT 5
    """), {"vector": vector})

    for row in result:
        print(row)

