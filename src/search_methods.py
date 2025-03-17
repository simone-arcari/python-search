import re
import PyPDF2
import docx

def search_in_txt(file_path, keyword):
    """Cerca la parola chiave in file di testo."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return any(keyword in line for line in f)
    except Exception:
        return False

def search_in_pdf(file_path, keyword):
    """Cerca la parola chiave in file PDF."""
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                if keyword.lower() in page.extract_text().lower():
                    return True
    except Exception:
        return False
    return False

def search_in_docx(file_path, keyword):
    """Cerca la parola chiave in file DOCX."""
    try:
        doc = docx.Document(file_path)
        return any(keyword in para.text for para in doc.paragraphs)
    except Exception:
        return False

def search_in_binary(file_path, keyword):
    """Cerca la parola chiave in un file binario a livello di byte."""
    keyword_bytes = keyword.encode()
    try:
        with open(file_path, "rb") as f:
            return keyword_bytes in f.read()
    except Exception:
        return False
