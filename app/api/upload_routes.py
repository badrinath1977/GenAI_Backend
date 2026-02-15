from fastapi import APIRouter, UploadFile, File
import shutil
import os
from app.ingestion.document_ingestor import DocumentIngestor
from app.services.vector_store_service import VectorStoreService

router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_DIR = "./data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/document")
async def upload_document(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingestor = DocumentIngestor()
    docs = ingestor.ingest(file_path)

    vector = VectorStoreService()
    vector.save(docs)

    return {"message": "Document processed and stored successfully"}
