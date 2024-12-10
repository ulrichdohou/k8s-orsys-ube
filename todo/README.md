# Todo List Application - Full Stack Deployment Guide

This guide provides step-by-step instructions to deploy a complete Todo List application with a microservices architecture, including:
- **Frontend**: React
- **API**: FastAPI (RESTful)
- **Database**: PostgreSQL

---

## Prerequisites

- Docker
- Kubernetes (Minikube or equivalent)
- `kubectl` configured
- Git

---

## Project Structure

```bash
labs/
├── api/       # Backend (FastAPI)
├── frontend/  # Frontend (React)
└── k8s/       # Kubernetes Manifests
    ├── namespace.yaml
    ├── postgres/
    ├── api/
    └── frontend/
```

---

## Deployment Steps

### 1. Build Docker Images

#### 1.1 Build the FastAPI Image
```bash
cd labs/api
docker build -t todo-api:latest .
```

#### 1.2 Build the React Image
```bash
cd ../frontend
docker build -t todo-frontend:latest .
```

---

### 2. Deploy to Kubernetes

#### 2.1 Create the Namespace
```bash
kubectl apply -f labs/k8s/namespace.yaml
```

#### 2.2 Deploy PostgreSQL
Create the resources for PostgreSQL:
```bash
kubectl apply -f labs/k8s/postgres/
```

#### 2.3 Deploy the API
```bash
kubectl apply -f labs/k8s/api/
```

#### 2.4 Deploy the Frontend
```bash
kubectl apply -f labs/k8s/frontend/
```

---

### 3. Verify Deployment

#### Check all resources:
```bash
kubectl get all -n todo-app
```

#### Check Pods:
```bash
kubectl get pods -n todo-app
```

#### Check Services:
```bash
kubectl get svc -n todo-app
```

---

### 4. Access the Application

The application is accessible via:
- **Frontend**: [http://localhost:30001](http://localhost:30001)
- **API**: [http://localhost:8000](http://localhost:8000) (direct access if needed)

---

## Monitoring and Logs

### View Pod Logs

#### Logs for the Frontend:
```bash
kubectl logs -n todo-app -l app=frontend
```

#### Logs for the API:
```bash
kubectl logs -n todo-app -l app=fastapi
```

#### Logs for PostgreSQL:
```bash
kubectl logs -n todo-app -l app=postgres
```

---

### Check Pod Status
```bash
kubectl describe pods -n todo-app
```

---

## Cleanup

To remove the application entirely:
```bash
kubectl delete namespace todo-app
```

---

## Important Notes

1. **Secrets**: Secrets are encoded in base64. For production, use a secure secrets manager.
2. **Persistent Volumes**: PersistentVolumeClaims (PVCs) retain data even after restarts.
3. **NodePort Access**: The application uses NodePort for easier access in development environments.

---

## Troubleshooting

1. **Pods not starting**:
   ```bash
   kubectl describe pod <pod-name> -n todo-app
   ```

2. **Database not accessible**:
   ```bash
   kubectl exec -it <postgres-pod> -n todo-app -- psql -U postgres
   ```

3. **Restarting a deployment**:
   ```bash
   kubectl rollout restart deployment <deployment-name> -n todo-app
   ```

---

Happy Developing with the Todo List App! 🚀