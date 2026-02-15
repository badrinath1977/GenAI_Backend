from app.services.vector_store_service import VectorStoreService
from app.services.llm_service import LLMService

class RAGOrchestrator:

    def __init__(self):
        self.vector = VectorStoreService()
        self.llm = LLMService()

    def ask(self, question):
        docs = self.vector.search(question)
        context = "\n".join([d.page_content for d in docs])
        prompt = f"Answer based on context:\n{context}\n\nQuestion: {question}"
        return self.llm.generate(prompt)
