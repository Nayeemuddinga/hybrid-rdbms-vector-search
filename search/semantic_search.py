SELECT *
FROM documents
WHERE content ILIKE '%failover%'
ORDER BY created_at DESC;

