
# NGINX Deployment Guide

  

This guide provides step-by-step instructions for deploying an NGINX application in a Kubernetes cluster and accessing it via a Service.

  

---

  

## Prerequisites

  

- A running Kubernetes cluster

-  `kubectl` installed and configured to access your cluster

  

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

  

### 3. Create the Service

Expose the NGINX deployment via a Service:

```bash

kubectl apply -f service.yaml

```

  

---

  

## Access the NGINX Service

  

### 4. Access the Service Locally

Start the `kubectl proxy` to access the Service locally:

```bash

kubectl proxy

```

  

Access the NGINX service using the following URL:

[http://localhost:8001/api/v1/namespaces/nginx-namespace/services/http:nginx-service:/proxy/](http://localhost:8001/api/v1/namespaces/nginx-namespace/services/http:nginx-service:/proxy/)

  

---

  

## Notes

  

- Ensure the Namespace, Deployment, and Service YAML files are correctly configured.

- Verify that the `kubectl proxy` command is running to access the Service locally.

  

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

  

---

  

Happy Hosting with NGINX! 🚀