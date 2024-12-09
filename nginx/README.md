
# NGINX Deployment Guide

This guide provides step-by-step instructions for deploying an NGINX application in a Kubernetes cluster, configuring autoscaling, and managing updates with a RollingUpdate strategy.

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
  replicas: 2
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
        image: nginx:1.26.2-alpine
        ports:
        - containerPort: 80
```

### 3. Describe the Deployment
View the details of the Deployment to confirm its current state:
```bash
kubectl describe deployment nginx-deployment -n nginx-namespace
```

---

## Autoscaling Configuration

### 4. Enable Horizontal Pod Autoscaler (HPA)
Configure an HPA to scale the NGINX deployment based on CPU utilization:
```bash
kubectl autoscale deployment nginx-deployment -n nginx-namespace --cpu-percent=50 --min=3 --max=10
```

### 5. Verify HPA Impact
Describe the Deployment to check the impact of the HPA configuration:
```bash
kubectl describe deployment nginx-deployment -n nginx-namespace
```

---

## Update Management

### 6. Rolling Update Strategy
Make changes to the Deployment (e.g., updating the image version), and Kubernetes will ensure a smooth rollout:
```bash
kubectl set image deployment/nginx-deployment -n nginx-namespace nginx=nginx:latest
```

### 7. Monitor Rollout Progress
Check the rollout status to ensure it completes successfully:
```bash
kubectl rollout status deployment/nginx-deployment -n nginx-namespace
```

### 8. View Rollout History
Check the history of Deployment revisions:
```bash
kubectl rollout history deployment/nginx-deployment -n nginx-namespace
```

### 9. Manual Rollback to a Specific Revision
Perform a rollback to a specific revision (e.g., revision 2):
```bash
kubectl rollout undo deployment/nginx-deployment -n nginx-namespace --to-revision=2
```

### 10. Verify Rollout Status After Rollback
Check the rollout status after the rollback:
```bash
kubectl rollout status deployment/nginx-deployment -n nginx-namespace
```

---

## Access the NGINX Service

### 11. Access the Service Locally
Start the `kubectl proxy` to access the Service locally:
```bash
kubectl proxy
```

Access the NGINX service using the following URL:
[http://localhost:8001/api/v1/namespaces/nginx-namespace/services/http:nginx-service:/proxy/](http://localhost:8001/api/v1/namespaces/nginx-namespace/services/http:nginx-service:/proxy/)

---

## Notes

- Use the `kubectl describe` command before and after HPA or updates to observe the changes and impact.
- Monitor CPU usage to observe HPA scaling behavior.
- The RollingUpdate strategy ensures no downtime during updates.
- Use `kubectl rollout undo` with the `--to-revision` option to revert to a specific version.

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

Happy Hosting and Scaling with NGINX! 🚀