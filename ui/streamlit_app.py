import streamlit as st
import requests

st.title("Enterprise RAG Assistant")

query = st.text_input("Ask something")

if st.button("Submit"):
    res = requests.post("http://localhost:8000/chat", json={"query": query})
    st.write(res.json())