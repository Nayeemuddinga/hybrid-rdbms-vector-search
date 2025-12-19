from fastapi import FastAPI
from app.query_agent import analyze_query

app = FastAPI()

@app.get("/search")
def search(q: str):
    strategy = analyze_query(q)
    return {"query": q, "strategy": strategy}

