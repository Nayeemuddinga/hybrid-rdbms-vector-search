def analyze_query(query):
    if "latest" in query:
        return "ORDER BY created_at DESC"
    if "similar" in query:
        return "VECTOR"
    return "KEYWORD"

