FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Default command for execute the script 
CMD ["python", "src/main.py"]
