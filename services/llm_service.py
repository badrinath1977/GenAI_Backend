from app.core.settings import settings
from langchain.llms import Ollama
from langchain.chat_models import ChatOpenAI

class LLMService:
    def __init__(self):
        if settings.LLM_PROVIDER.lower() == "openai":
            self.llm = ChatOpenAI(
                openai_api_key=settings.OPENAI_API_KEY,
                model=settings.OPENAI_MODEL
            )
        else:
            self.llm = Ollama(model=settings.OLLAMA_MODEL)

    def generate(self, prompt: str):
        return self.llm.invoke(prompt)
