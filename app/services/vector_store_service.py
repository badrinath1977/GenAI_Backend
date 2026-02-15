from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from app.core.settings import settings
import os

class VectorStoreService:

    def __init__(self):
        if settings.LLM_PROVIDER.lower() == "openai":
            self.embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
        else:
            self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        if os.path.exists(settings.VECTOR_DB_PATH):
            self.db = FAISS.load_local(settings.VECTOR_DB_PATH, self.embeddings)
        else:
            self.db = None

    def save(self, docs):
        self.db = FAISS.from_documents(docs, self.embeddings)
        self.db.save_local(settings.VECTOR_DB_PATH)

    def search(self, query, k=3):
        if not self.db:
            return []
        return self.db.similarity_search(query, k=k)
