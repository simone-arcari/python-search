import os

def get_file_extension(file_name):
    """Restituisce l'estensione del file senza il punto."""
    _, ext = os.path.splitext(file_name)
    return ext.lower().lstrip(".")  # Rimuove il punto (.) dall'estensione
