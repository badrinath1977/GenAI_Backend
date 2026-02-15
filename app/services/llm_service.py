from langchain.llms import Ollama
from app.core.settings import settings

class LLMService:
    def __init__(self):
        self.llm = Ollama(model=settings.LLM_MODEL)

    def generate(self, prompt: str):
        return self.llm.invoke(prompt)
