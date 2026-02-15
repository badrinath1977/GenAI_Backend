import os
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredExcelLoader,
    UnstructuredPowerPointLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from PIL import Image
import pytesseract


class DocumentIngestor:

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

    def ingest(self, file_path: str):

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            loader = PyPDFLoader(file_path)
            docs = loader.load()

        elif extension == ".docx":
            loader = UnstructuredWordDocumentLoader(file_path)
            docs = loader.load()

        elif extension == ".xlsx":
            loader = UnstructuredExcelLoader(file_path)
            docs = loader.load()

        elif extension == ".pptx":
            loader = UnstructuredPowerPointLoader(file_path)
            docs = loader.load()

        elif extension == ".txt":
            loader = TextLoader(file_path)
            docs = loader.load()

        elif extension in [".png", ".jpg", ".jpeg"]:
            text = self._extract_text_from_image(file_path)
            docs = [{"page_content": text, "metadata": {"source": file_path}}]

        else:
            raise ValueError(f"Unsupported file type: {extension}")

        return self.splitter.split_documents(docs)

    def _extract_text_from_image(self, file_path):
        image = Image.open(file_path)
        return pytesseract.image_to_string(image)
