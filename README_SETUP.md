# Enterprise RAG Backend (Clean Version)

## Architecture Flow

User → FastAPI → RAGOrchestrator  
RAGOrchestrator → VectorStoreService → EmbeddingService  
RAGOrchestrator → LLMService  
Response → User

## Setup

1. python -m venv venv

2. Activate environment
Windows:
venv\Scripts\activate



3. pip install -r requirements.txt

4. Install Ollama and pull model
ollama pull llama3.2:1b

5. Run application
uvicorn app.main:app --reload

6. Open Swagger
http://localhost:8000/docs

## Environment Variables (.env)

CHROMA_DB_PATH=./data/chroma
EMBEDDING_MODEL=all-MiniLM-L6-v2
LLM_MODEL=llama3.2:1b


# delete env 
-- Remove-Item -Recurse -Force .\genai_svc_env
-- python -m venv genai_svc_env --clear

# uninstall 
-- pip freeze > uninstall.txt
-- pip uninstall -r uninstall.txt -y


