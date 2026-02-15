from langchain.embeddings import HuggingFaceEmbeddings
from app.core.settings import settings

class EmbeddingService:
    def __init__(self):
        self.model = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)

    def embed(self, text: str):
        return self.model.embed_query(text)
