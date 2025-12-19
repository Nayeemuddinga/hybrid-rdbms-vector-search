CREATE TABLE embedding_audit (
    doc_id UUID,
    model_name TEXT,
    embedding_version TEXT,
    created_at TIMESTAMP,
    created_by TEXT
);

