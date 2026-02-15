from app.core.settings import settings
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama


class LLMService:

    def __init__(self):
        provider = settings.LLM_PROVIDER.lower()

        if provider == "openai":
            self.llm = ChatOpenAI(
                api_key=settings.OPENAI_API_KEY,
                model=settings.OPENAI_MODEL
            )

        elif provider == "ollama":
            self.llm = Ollama(
                model=settings.OLLAMA_MODEL
            )

        else:
            raise ValueError(f"Unsupported LLM_PROVIDER: {provider}")

    def generate(self, prompt: str):
        return self.llm.invoke(prompt)

