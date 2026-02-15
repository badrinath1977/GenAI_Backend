
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_orchestrator import RAGOrchestrator

router = APIRouter()
rag = RAGOrchestrator()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
def chat(request: ChatRequest):
    response = rag.ask(request.question)
    return {"response": response}
