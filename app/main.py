from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Enterprise RAG Backend")

app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}
