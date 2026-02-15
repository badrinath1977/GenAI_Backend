from app.services.vector_store_service import VectorStoreService
from app.services.llm_service import LLMService

class RAGOrchestrator:
    def __init__(self):
        self.vector_service = VectorStoreService()
        self.llm_service = LLMService()

    def ask(self, query: str):
        docs = self.vector_service.similarity_search(query)
        context = "\n".join([doc.page_content for doc in docs])
        prompt = f"Answer based on context:\n{context}\n\nQuestion: {query}"
        return self.llm_service.generate(prompt)
