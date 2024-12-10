#!/bin/bash

# S'assurer d'être dans le contexte Docker de minikube
eval $(minikube docker-env)

# Construire l'image avec l'argument
docker build --build-arg VITE_API_URL=http://localhost:30051  -t todo-frontend:latest . 