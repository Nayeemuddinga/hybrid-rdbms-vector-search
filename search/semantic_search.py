#SELECT *
FROM documents
WHERE content ILIKE '%failover%'
ORDER BY created_at DESC; #

ORDER BY embedding <=> :vector LIMIT 5;
