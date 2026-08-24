# Task Tracker - Kubernetes DevOps Pipeline

This project demonstrates a complete DevOps pipeline for a full-stack Task Tracker application. It features a FastAPI backend connected to a PostgreSQL database, all containerized and orchestrated using Kubernetes. The project includes local environment provisioning using Terraform.

## Project Structure

- **`main.py`**: The FastAPI application source code, utilizing SQLAlchemy for database ORM.
- **`Dockerfile`**: Container image definition for the Task Tracker API.
- **`k8s-manifests/`**: Kubernetes configuration files for deployment:
  - `deployment.yaml` & `service.yaml`: API deployment and NodePort service.
  - `postgres-statefulset.yaml` & `postgres-service.yaml`: PostgreSQL database StatefulSet and headless service.
  - `postgres-pvc.yaml`: Persistent Volume Claim for database storage.
  - `postgres-configmap.yaml` & `postgres-secret.yaml`: Environment variables and credentials.
- **`terraform-local/`**: Terraform configurations to provision the local Kubernetes cluster environment (e.g., using `kind`).
- **`.github/`**: GitHub Actions workflows for continuous integration and delivery.

## Architecture

1.  **API Layer**: Built with **FastAPI** (Python). Exposes REST endpoints to manage tasks.
2.  **Database**: **PostgreSQL** deployed as a StatefulSet with persistent storage to ensure data durability across pod restarts.
3.  **Containerization**: **Docker** is used to package the API.
4.  **Orchestration**: **Kubernetes** handles scaling, networking, and secrets management.
5.  **Infrastructure as Code**: **Terraform** provisions the local cluster infrastructure.

## Local Development Setup

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Kubernetes CLI (`kubectl`)](https://kubernetes.io/docs/tasks/tools/)
- [Terraform](https://developer.hashicorp.com/terraform/downloads)

### 1. Provision the Local Cluster

Navigate to the terraform directory and initialize the environment:

```bash
cd terraform-local
terraform init
terraform apply
```

### 2. Deploy to Kubernetes

Apply the Kubernetes manifests to create the database, secrets, and the API deployment:

```bash
cd ../
kubectl apply -f k8s-manifests/
```

Verify that all pods are running:

```bash
kubectl get pods
```

### 3. Access the Application

The API is exposed via a NodePort service. You can set up a port-forward to access it locally:

```bash
kubectl port-forward svc/task-tracker-service 8080:80
```

You can now access the interactive API documentation at:
**[http://localhost:8080/docs](http://localhost:8080/docs)**

## API Endpoints

- `GET /health`: Health check endpoint for Kubernetes liveness/readiness probes.
- `GET /tasks`: Retrieve all tasks from the database.
- `POST /tasks`: Create a new task.

## Future Enhancements

- Integrate a frontend SPA (React/Vue/Svelte).
- Add Ingress controller for production-grade routing.
- Implement comprehensive unit and integration testing.
- Set up monitoring and alerting (Prometheus + Grafana).
