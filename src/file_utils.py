import os
import logging

def get_file_extension(file_name) -> str:
    """Restituisce l'estensione del file senza il punto."""
    _, ext = os.path.splitext(file_name)
    result = ext.lower().lstrip(".")  # Rimuove il punto (.) dall'estensione
    logging.debug("file extension: " + result)
    return result

def contains_keyword_in_filename(keyword, file_path) -> bool:
    """Verifica se la parola chiave è presente nel nome del file."""
    file_name = os.path.basename(file_path)  # Ottieni il nome del file senza il percorso
    logging.debug("filename: " + file_name + ", keyword: " + keyword)
    is_contained = keyword.lower() in file_name.lower()  # Confronta in modo case-insensitive
    logging.debug("is  keyword contained in filename: " + str(is_contained))
    return is_contained
