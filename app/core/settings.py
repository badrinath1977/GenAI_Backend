from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    CHROMA_DB_PATH: str = "./data/chroma"
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    LLM_MODEL: str = "llama3.2:1b"
    
    class Config:
        env_file = ".env"

settings = Settings()
