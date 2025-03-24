#!/bin/bash

# Define the names for the Docker images and containers
IMAGE1="server_image"
CONTAINER1="server"

IMAGE2="client_image"
CONTAINER2="client"

NETWORK="python-net"

# Build the Docker images
echo "Building Docker image for Server..."
docker build -t $IMAGE1 -f Server/Dockerfile Server

echo "Building Docker image for Client..."
docker build -t $IMAGE2 -f Client/Dockerfile Client

# Create a Docker network
echo "Creating Docker network..."
docker network create $NETWORK

# Run the Docker containers
echo "Running Server container..."
docker run -d -p 5000:5000 --name $CONTAINER1 --network $NETWORK --device /dev/video0:/dev/video0 $IMAGE1


echo "Running Client container..."
docker run -d -p 8000:8000 --name $CONTAINER2 --network $NETWORK $IMAGE2

echo "Containers are up and running!"
