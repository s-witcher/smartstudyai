import os
from PyPDF2 import PdfReader

def ingest_file(file_path: str) -> str:
    """
    Reads a PDF or text file and returns its content as text.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")

    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()

    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    else:
        raise ValueError("Unsupported file type. Use .pdf or .txt")
