minikube start --driver=docker --nodes=1 --profile=control-plane-1

minikube node add worker-1 --profile=control-plane-1
minikube node add worker-2 --profile=control-plane-1
minikube node add worker-3 --profile=control-plane-1
minikube node add worker-4 --profile=control-plane-1
minikube node add worker-5 --profile=control-plane-1

kubectl get nodes

kubectl create deployment nginx --image=nginx --replicas=3

kubectl get deployments

kubectl get pods

kubectl expose deployment nginx --type=NodePort --port=80

minikube service nginx --url
