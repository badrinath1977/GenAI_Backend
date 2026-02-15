from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from app.core.settings import settings
import os


class VectorStoreService:

    def __init__(self):

        provider = settings.EMBEDDING_PROVIDER.lower()

        if provider == "openai":
            self.embeddings = OpenAIEmbeddings(
                api_key=settings.OPENAI_API_KEY
            )

        elif provider == "local":
            self.embeddings = HuggingFaceEmbeddings(
                model_name="all-MiniLM-L6-v2"
            )

        else:
            raise ValueError(f"Unsupported EMBEDDING_PROVIDER: {provider}")

        if os.path.exists(settings.VECTOR_DB_PATH):
            self.db = FAISS.load_local(
                settings.VECTOR_DB_PATH,
                self.embeddings,
                allow_dangerous_deserialization=True
            )
        else:
            self.db = None

    def save(self, docs):
        self.db = FAISS.from_documents(docs, self.embeddings)
        self.db.save_local(settings.VECTOR_DB_PATH)

    def search(self, query, k=3):
        if not self.db:
            return []
        return self.db.similarity_search(query, k=k)
