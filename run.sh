#!/bin/bash

IMAGE_NAME="ricerca-file"
CONTAINER_NAME="ricerca-file-container"

# Controlla se l'immagine Docker esiste già
if ! docker images | grep -q "$IMAGE_NAME"; then
    echo "🔨 Costruzione dell'immagine Docker..."
    docker build -t "$IMAGE_NAME" .
else
    echo "✅ L'immagine Docker esiste già."
fi

# Esegui il container
echo "🚀 Avvio del container..."
docker run -it --rm -v "$(pwd)":/app "$IMAGE_NAME"
