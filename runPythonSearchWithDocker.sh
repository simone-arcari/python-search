#!/bin/bash

IMAGE_NAME="python-search"
CONTAINER_NAME="python-search-container"

# Controlla se l'immagine Docker esiste già
if ! docker images | grep -q "$IMAGE_NAME"; then
    echo "🔨 Building docker image..."
    docker build -t "$IMAGE_NAME" .
    echo "✅ Docker image built."
else
    echo "✅ Docker image already exists."
fi

# Esegui il container
echo "🚀 Starting container..."
# docker run -it --rm "$IMAGE_NAME"
docker run -it --rm "$IMAGE_NAME"
