import os
import shutil
from search_methods import search_in_txt, search_in_pdf, search_in_docx, search_in_binary
from file_utils import get_file_extension

class KeywordSearcher:
    def __init__(self, keyword, search_path, output_path):
        self.keyword = keyword
        self.search_path = search_path
        self.output_path = output_path
        self.files_found = []
        self.search_methods = {
            "txt": search_in_txt,
            "pdf": search_in_pdf,
            "docx": search_in_docx,
        }

    def search_keyword(self):
        """Naviga la directory e cerca la parola chiave nei file."""
        for root, _, files in os.walk(self.search_path):
            for file in files:
                file_path = os.path.join(root, file)
                extension = get_file_extension(file)

                # Se l'estensione ha un metodo associato, lo eseguiamo
                if extension in self.search_methods:
                    found = self.search_methods[extension](file_path, self.keyword)
                else:
                    # Se non ha estensione, usiamo la ricerca in formato binario
                    found = search_in_binary(file_path, self.keyword)

                # Se la keyword è stata trovata, inseriamo il file in lista
                if found:
                    self.files_found.append(file_path)

        # copiamo tutti i file trovati
        for file in self.files_found:           
            self.copy_to_output(file)

    def copy_to_output(self, file_path):
        """Copia il file nella directory di output."""
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        shutil.copy(file_path, self.output_path)
        print(f"Copied: {file_path} -> {self.output_path}")

    def print_result(self):
        print("Search Result:")
        for file in self.files_found:
            print("\t"+file)
