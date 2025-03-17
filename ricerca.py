import os
import shutil
import PyPDF2
import docx

def search_in_text_file(file_path, keyword):
    """Cerca la parola chiave in un file di testo."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if keyword.lower() in line.lower():
                    return True
    except Exception:
        pass
    return False

def search_in_pdf(file_path, keyword):
    """Cerca la parola chiave in un file PDF."""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                if page.extract_text() and keyword.lower() in page.extract_text().lower():
                    return True
    except Exception:
        pass
    return False

def search_in_docx(file_path, keyword):
    """Cerca la parola chiave in un file DOCX."""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            if keyword.lower() in para.text.lower():
                return True
    except Exception:
        pass
    return False

def search_keyword(keyword, search_dir, output_dir):
    """Cerca la parola chiave nei nomi e nei contenuti dei file e li copia nella directory di output."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, _, files in os.walk(search_dir):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Controllo se la parola chiave è nel nome del file
            if keyword.lower() in file.lower():
                shutil.copy(file_path, output_dir)
                continue
            
            # Controllo nel contenuto del file
            if file.endswith('.txt') and search_in_text_file(file_path, keyword):
                shutil.copy(file_path, output_dir)
            elif file.endswith('.pdf') and search_in_pdf(file_path, keyword):
                shutil.copy(file_path, output_dir)
            elif file.endswith('.docx') and search_in_docx(file_path, keyword):
                shutil.copy(file_path, output_dir)

def main():
    param1 = input("Inserisci la parola da cercare: ")
    param2 = input("Inserisci la directory di partenza: ")
    param3 = input("Inserisci la directory di output: ")
    
    if not os.path.isdir(param2):
        print("Errore: la directory di partenza non esiste.")
        return
    
    search_keyword(param1, param2, param3)
    print("Ricerca completata. I file trovati sono stati copiati nella directory di output.")

if __name__ == "__main__":
    main()
