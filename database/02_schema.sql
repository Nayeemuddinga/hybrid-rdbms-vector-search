CREATE TABLE documents (
    doc_id UUID PRIMARY KEY,
    title TEXT,
    content TEXT,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE document_embeddings (
    doc_id UUID REFERENCES documents(doc_id),
    embedding VECTOR(1536),
    embedding_version TEXT,
    created_at TIMESTAMP DEFAULT now()
);

