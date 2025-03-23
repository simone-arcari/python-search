FROM python:3.10

WORKDIR /app

COPY /src /app/src
COPY docker/enviromentWithSomeFile/ /app/enviromentWithSomeFile
COPY docker/offline_packages/ /app/offline_packages
COPY requirements.txt .

# Install pre-downloaded requirements
RUN pip install --no-cache-dir --find-links=/app/offline_packages -r requirements.txt

RUN mkdir outputPythonSearch/
RUN ls


# Default command for execute the script 
CMD ["python", "src/main.py", "pippo", "enviromentWithSomeFile/", "outputPythonSearch/"]
