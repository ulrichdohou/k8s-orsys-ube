# Todo List Application - Full Stack Deployment Guide

Cette application Todo List est une application full-stack avec les fonctionnalités suivantes :
- **Frontend**: React avec Tailwind CSS
  - Interface utilisateur moderne et responsive
  - Pagination des todos
  - Confirmation de suppression via modal
  - Formulaire stylisé
- **API**: FastAPI (RESTful)
  - Pagination côté serveur
  - CRUD operations
  - Validation des données
- **Database**: PostgreSQL

---

## Prerequisites

- Docker
- Kubernetes (Minikube ou équivalent)
- `kubectl` configuré
- Git
- Node.js (pour le développement)

---

## Project Structure

```bash
labs/
├── api/                 # Backend (FastAPI)
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py     # API endpoints
│   │   ├── models.py   # Database models
│   │   └── database.py # Database configuration
│   └── Dockerfile
├── frontend/           # Frontend (React)
│   ├── src/
│   │   ├── App.jsx    # Application principale
│   │   └── main.jsx   # Point d'entrée
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── Dockerfile
└── k8s/               # Kubernetes Manifests
    ├── namespace.yaml
    ├── postgres/
    ├── api/
    └── frontend/
```

---

## Deployment Steps

### 1. Configuration de l'environnement

```bash
# Démarrer minikube
minikube start

# Activer le tunnel minikube (dans un terminal séparé)
minikube tunnel
```

### 2. Build Docker Images

#### 2.1 Build l'image FastAPI
```bash
eval $(minikube docker-env)
cd labs/api
docker build -t todo-api:latest .
```

#### 2.2 Build l'image React
```bash
cd ../frontend
./build.sh  # Script qui inclut les variables d'environnement
```

---

### 3. Deploy to Kubernetes

#### 3.1 Create Namespace
```bash
kubectl apply -f labs/k8s/namespace.yaml
```

#### 3.2 Deploy PostgreSQL
```bash
kubectl apply -f labs/k8s/postgres/
```

#### 3.3 Deploy API
```bash
kubectl apply -f labs/k8s/api/
```

#### 3.4 Deploy Frontend
```bash
kubectl apply -f labs/k8s/frontend/
```

---

### 4. Access the Application

L'application est accessible via :
- **Frontend**: http://localhost:30052
- **API**: http://localhost:30051

---

## API Endpoints

### Todos
- `GET /todos?page=1&limit=5` - Liste paginée des todos
- `POST /todos` - Créer un nouveau todo
- `DELETE /todos/{id}` - Supprimer un todo

---

## Frontend Features

1. **Interface utilisateur**
   - Design moderne avec Tailwind CSS
   - Formulaire de création intuitif
   - Table responsive pour l'affichage des todos

2. **Pagination**
   - Navigation par page
   - Affichage du nombre total de pages
   - Limite configurable d'items par page

3. **Interactions utilisateur**
   - Modal de confirmation pour la suppression
   - Feedback visuel des actions
   - Validation des formulaires

---

## Monitoring and Logs

### View Pod Logs
```bash
# Logs Frontend
kubectl logs -n todo-app -l app=frontend

# Logs API
kubectl logs -n todo-app -l app=fastapi

# Logs PostgreSQL
kubectl logs -n todo-app -l app=postgres
```

---

## Cleanup

Pour supprimer l'application :
```bash
kubectl delete namespace todo-app
```

---

## Troubleshooting

1. **Problèmes de connexion à l'API**
   ```bash
   kubectl get svc -n todo-app
   kubectl describe svc fastapi -n todo-app
   ```

2. **Problèmes de base de données**
   ```bash
   kubectl exec -it <postgres-pod> -n todo-app -- psql -U postgres
   ```

3. **Redémarrage des services**
   ```bash
   kubectl rollout restart deployment frontend fastapi -n todo-app
   ```

---

Happy Coding! 🚀