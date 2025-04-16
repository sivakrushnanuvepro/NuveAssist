from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

api_key = st.secrets["GOOGLE_API_KEY"]
#api_key = os.getenv("GOOGLE_API_KEY")

import os
from dotenv import load_dotenv
load_dotenv()

def load_rag_chain():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=api_key)
    db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

    retriever = db.as_retriever()

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",google_api_key=os.getenv("GOOGLE_API_KEY"),)
    rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return rag_chain
