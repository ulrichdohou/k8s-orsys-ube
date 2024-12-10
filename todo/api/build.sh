#!/bin/bash

# S'assurer d'être dans le contexte Docker de minikube
eval $(minikube docker-env)

# Construire l'image avec l'argument
docker build -t todo-api:latest . 