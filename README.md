# Python Search
All'interno di [src/] si trovano tutti i file del programma scritto in python.
Questo programma cerca una keyword all'interno dei file o nel nome stesso del file.
La ricerca naviga tutti i path all'interno del path di ricerca fornito.

Il programma prende 4 input:
[arg1]: -> <keyword_da_cercare>
[arg2]: -> <path_in_cui_cercare>
[arg3]: -> <path_in_cui_copiare_i_file_contenenti_la_keyword>
[arg4]: -> <livello_di_log>

il livello di log deve essere uno tra [INFO] e [DEBUG]

## Esempio:

aprire un terminale e portarsi all'interno della cartella [python-search/]

lanciare il programma:

python src/main.py pippo path_ricerca path_output INFO

[arg1]: -> <pippo>
[arg2]: -> <path_ricerca>
[arg3]: -> <path_output>
[arg4]: -> <INFO>

abbiamo cosi lanciato la ricerca della keyword "pippo" all'interno della cartella chimata path_ricerca.
Vedremo i file con la keyword "pippo" copiati dentro la cartella path_output.
Il livello di log è stato impostato su INFO

## Docker
Per provare il funzionamento del programma in ambiente fornito di tutte le dipendenze e svincolato dal proprio pc.
Nel container vengono copiati dei file che contengono la keyword "pippo".
Dentro il conatiner viene avviato il programma python che troverà i file e li copierà in una cartella dentro il containe.

Per usare docker:

sudo ./runPythonSearchWithDocker.sh

L'output atteso è:

2025-03-23 10:48:04 - INFO - print_result - ################# Search Result ###############
2025-03-23 10:48:04 - INFO - print_result -     enviromentWithSomeFile/ciao-pippo.txt
2025-03-23 10:48:04 - INFO - print_result -     enviromentWithSomeFile/tabella.csv
2025-03-23 10:48:04 - INFO - print_result -     enviromentWithSomeFile/folder1/ciao.txt
2025-03-23 10:48:04 - INFO - print_result -     enviromentWithSomeFile/folder2/dir/example.pdf

