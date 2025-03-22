FROM python:3.10

WORKDIR /app

COPY /src /app
COPY /enviromentWithSomeFile /app

RUN pip install --no-cache-dir -r requirements.txt

# Default command for execute the script 
CMD ["python", "src/main.py", "pippo", ".", "tmp/"]
