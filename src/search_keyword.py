import os
import shutil
from search_methods import search_in_txt, search_in_pdf, search_in_docx, search_in_binary
from file_utils import get_file_extension, contains_keyword_in_filename
import logging

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
        logging.info("searching keyword...")
        for root, _, files in os.walk(self.search_path):
            for file in files:
                file_path = os.path.join(root, file)
                extension = get_file_extension(file)

                # Se il nome del file contiene la keyword
                if contains_keyword_in_filename(self.keyword, file_path):
                    logging.debug("keyword found in filename - skip serching keyword inside the file")
                    found = True
                elif extension in self.search_methods:
                    # Se l'estensione ha un metodo associato per la ricerca, lo eseguiamo
                    logging.debug("found method to search keyword for a specific file extension")
                    found = self.search_methods[extension](file_path, self.keyword)
                else:
                    # Se non ha estensione, usiamo la ricerca in formato binario
                    logging.debug("search keyword whit in binary format into the file")
                    found = search_in_binary(file_path, self.keyword)

                # Se la keyword è stata trovata, inseriamo il file in lista
                if found:
                    logging.info("SUCCESS: keyword found!!!")
                    self.files_found.append(file_path)

        # copiamo tutti i file trovati
        for file in self.files_found:
            logging.info("copy file whit keyword in output path")         
            self._copy_to_output(file)

    def _copy_to_output(self, file_path):
        """Copia il file nella directory di output."""
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        shutil.copy(file_path, self.output_path)
        print(f"Copied: {file_path} -> {self.output_path}")

    def _copy_to_output(self, file_path):
        """Copia il file nella directory di output, gestendo l'eccezione se il file esiste già."""
        try:
            if not os.path.exists(self.output_path):
                logging.warning("the file is alredy in output path")
                os.makedirs(self.output_path)
            shutil.copy(file_path, self.output_path)
            logging.info(f"Copied: {file_path} -> {self.output_path}")
        except shutil.SameFileError:
            destination_file = os.path.join(self.output_path, os.path.basename(file_path))
            logging.debug(f"Errore: il file {destination_file} è lo stesso del file di origine. Ignoro la copia.")
        except Exception as e:
            logging.critical(f"Errore imprevisto durante la copia: {e}")

    def print_result(self):
        logging.info("################# Search Result ###############")
        for file in self.files_found:
            logging.info("\t"+file)
