from fastapi import FastAPI
from pydantic import BaseModel
from rag_chain import load_rag_chain
from fastapi.middleware.cors import CORSMiddleware
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load RAG chain
rag_chain = load_rag_chain()

# ✅ Define request model (aligned with JSON key: "question")
class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(item: Question):
    logging.info(f"📥 Received query: {item.question}")
    try:
        # create a simple promt and pass it to the chain
        prompt = f"Give me the solution in points for the question. Also tell like you are not under 100% sure. for the question: {item.question}"
        logging.info(f"🔍 Prompt: {prompt}")

        response = rag_chain.run(prompt)
        logging.info(f"📤 Response: {response}")
        return {"answer": response}
    except Exception as e:
        logging.exception("❌ Error while processing query")
        return {"error": str(e)}
