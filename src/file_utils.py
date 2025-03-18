import os

def get_file_extension(file_name):
    """Restituisce l'estensione del file senza il punto."""
    _, ext = os.path.splitext(file_name)
    return ext.lower().lstrip(".")  # Rimuove il punto (.) dall'estensione

def contains_keyword_in_filename(keyword, file_path):
    """Verifica se la parola chiave è presente nel nome del file."""
    file_name = os.path.basename(file_path)  # Ottieni il nome del file senza il percorso
    return keyword.lower() in file_name.lower()  # Confronta in modo case-insensitive
