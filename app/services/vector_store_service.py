from langchain.vectorstores import Chroma
from app.core.settings import settings
from app.services.embedding_service import EmbeddingService

class VectorStoreService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.db = Chroma(
            persist_directory=settings.CHROMA_DB_PATH,
            embedding_function=self.embedding_service.model
        )

    def similarity_search(self, query: str, k: int = 3):
        return self.db.similarity_search(query, k=k)
