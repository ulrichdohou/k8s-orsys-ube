# NGINX Deployment Guide

This guide provides step-by-step instructions for deploying an NGINX application in a Kubernetes cluster, configuring autoscaling, and ensuring smooth updates with a RollingUpdate strategy.

---

## Prerequisites

- A running Kubernetes cluster
- `kubectl` installed and configured to access your cluster

---

## Deployment Steps

### 1. Create the Namespace
Create a Namespace for the NGINX deployment:
```bash
kubectl apply -f namespace.yaml
```

### 2. Deploy the NGINX Application
Apply the Deployment manifest to create the NGINX Pods:
```bash
kubectl apply -f deployment.yaml
```

The Deployment manifest includes a **RollingUpdate** strategy:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: nginx-namespace
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```

### 3. Create the Service
Expose the NGINX deployment via a Service:
```bash
kubectl apply -f service.yaml
```

---

## Autoscaling Configuration

### 4. Enable Horizontal Pod Autoscaler (HPA)
Configure an HPA to scale the NGINX deployment based on CPU utilization:
```bash
kubectl autoscale deployment nginx-deployment -n nginx-namespace --cpu-percent=50 --min=3 --max=10
```

### 5. Verify HPA
Check the status of the HPA to ensure it is active:
```bash
kubectl get hpa -n nginx-namespace
```

---

## Access the NGINX Service

### 6. Access the Service Locally
Start the `kubectl proxy` to access the Service locally:
```bash
kubectl proxy
```

Access the NGINX service using the following URL:
[http://localhost:8001/api/v1/namespaces/nginx-namespace/services/http:nginx-service:/proxy/](http://localhost:8001/api/v1/namespaces/nginx-namespace/services/http:nginx-service:/proxy/)

---

## Notes

- Ensure the Namespace, Deployment, and Service YAML files are correctly configured.
- Monitor CPU usage to observe HPA scaling behavior.

---

## Troubleshooting

- Check the status of the Pods in the Namespace:
  ```bash
  kubectl get pods -n nginx-namespace
  ```

- Check the logs of the NGINX Pods:
  ```bash
  kubectl logs <nginx-pod-name> -n nginx-namespace
  ```

- Verify the Service configuration:
  ```bash
  kubectl get services -n nginx-namespace
  ```

- View HPA metrics for scaling:
  ```bash
  kubectl describe hpa nginx-deployment -n nginx-namespace
  ```

---

Happy Hosting with NGINX! 🚀