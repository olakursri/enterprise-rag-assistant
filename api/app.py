from fastapi import FastAPI
from retrieval.rag_retriever import get_retriever

app = FastAPI()

@app.post("/chat")
def chat(query: str):
    # dummy response (replace with real chain)
    return {"response": f"Answer for: {query}"}