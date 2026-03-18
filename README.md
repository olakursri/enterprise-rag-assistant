# Enterprise RAG Knowledge Assistant

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system to enable enterprise document querying using LLMs.

## Architecture

User → UI → Backend API → Retriever → Vector DB → LLM → Response

## Tech Stack

* Python
* FastAPI
* LangChain
* FAISS / Pinecone
* OpenAI / Claude

## Features

* Document ingestion (PDF)
* Embedding generation
* Vector search
* LLM-based response generation

## How to Run

```bash
pip install -r requirements.txt
uvicorn api.app:app --reload
streamlit run ui/streamlit_app.py
```

## Use Cases

* Enterprise knowledge assistant
* Policy Q&A
* Internal documentation chatbot

## Future Enhancements

* Add authentication
* Add multi-document support
* Add feedback loop

* https://python.langchain.com
* https://platform.openai.com
