from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_orchestrator import RAGOrchestrator

router = APIRouter(prefix="/chat", tags=["Chat"])
rag = RAGOrchestrator()

class ChatRequest(BaseModel):
    question: str

@router.post("/ask")
def ask(req: ChatRequest):
    response = rag.ask(req.question)
    return {"response": str(response)}
