# from fastapi import FastAPI
# from retrieval.rag_retriever import get_retriever

# app = FastAPI()

# @app.post("/chat")
# def chat(query: str):
#     # dummy response (replace with real chain)
#     return {"response": f"Answer for: {query}"}

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    query: str
@app.get("/")
def root():
    return {"message": "RAG API is running 🚀"}
@app.post("/chat")
def chat(request: ChatRequest):
    return {"response": f"Answer for: {request.query}"}