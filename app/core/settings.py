# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     LLM_PROVIDER: str = "openai"  # openai or ollama
#     OPENAI_API_KEY: str = ""
#     OPENAI_MODEL: str = "gpt-4o-mini"
#     OLLAMA_MODEL: str = "llama3.2:1b"
#     VECTOR_DB_PATH: str = "./data/vectorstore"

#     class Config:
#         env_file = ".env"

# settings = Settings()


from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    LLM_PROVIDER: str = "ollama"
    EMBEDDING_PROVIDER: str = "local"

    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4o-mini"

    OLLAMA_MODEL: str = "llama3.2:1b"

    VECTOR_DB_PATH: str = "./data/vectorstore"

    class Config:
        env_file = ".env"


settings = Settings()
