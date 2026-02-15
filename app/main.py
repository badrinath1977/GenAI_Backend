from fastapi import FastAPI
from app.api.chat_routes import router as chat_router
from app.api.upload_routes import router as upload_router

app = FastAPI(title="Enterprise GenAI Backend")

app.include_router(chat_router)
app.include_router(upload_router)

@app.get("/health")
def health():
    return {"status": "healthy"}
