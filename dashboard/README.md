# Kubernetes Dashboard Deployment Guide

This guide provides step-by-step instructions for deploying and accessing the Kubernetes Dashboard.

---

## Prerequisites

- A running Kubernetes cluster
- `kubectl` installed and configured to access your cluster

---

## Deployment Steps

### 1. Download the Kubernetes Dashboard Manifest
Download the recommended deployment YAML file:
```bash
curl -L https://raw.githubusercontent.com/kubernetes/dashboard/v2.6.1/aio/deploy/recommended.yaml -o dashboard.yaml
```

### 2. Deploy the Kubernetes Dashboard
Apply the downloaded YAML file to deploy the Dashboard:
```bash
kubectl apply -f dashboard.yaml
```

### 3. Verify Deployment
Check all resources in the `kubernetes-dashboard` namespace:
```bash
kubectl get all -n kubernetes-dashboard
```

---

## User Configuration

### 4. Create a Service Account
Apply the Service Account configuration file:
```bash
kubectl apply -f dashboard-user.yaml
```

### 5. Create a Service Account Token
Apply the Token configuration file:
```bash
kubectl apply -f dashboard-user-token.yaml
```

### 6. Create a ClusterRoleBinding
Bind the Service Account to the required Cluster Role:
```bash
kubectl apply -f dashboard-clusterrolebinding.yaml
```

### 7. Retrieve the Token
Get the access token for the Service Account:
```bash
kubectl get secret dashboard-user-token -n kubernetes-dashboard -o jsonpath={.data.token} | base64 --decode > secret.txt
```

---

## Access the Dashboard

### 8. Start the Proxy
Start the `kubectl proxy` to enable local access:
```bash
kubectl proxy
```

### 9. Open the Dashboard
Access the Dashboard via the following URL:
[http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/](http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/)

---

## Notes

- Use the token retrieved in **Step 7** to log in to the Dashboard.
- Ensure your cluster allows access to the required ports and permissions.

---

## Troubleshooting

- If you encounter issues with the proxy, ensure `kubectl proxy` is running and accessible on your host.
- Check the logs of the Dashboard Pod for errors:
  ```bash
  kubectl logs -n kubernetes-dashboard <dashboard-pod-name>
  ```

---

Happy Kubernetes Dashboarding! 🚀