def fuse_scores(vector_results, keyword_results):
    scores = {}
    for r in vector_results:
        scores[r["doc_id"]] = scores.get(r["doc_id"], 0) + 0.6
    for r in keyword_results:
        scores[r["doc_id"]] = scores.get(r["doc_id"], 0) + 0.4
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

