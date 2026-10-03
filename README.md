# Advanced DevOps Lab 1: GitOps Pipeline with ArgoCD

Lab assignment for the Advanced DevOps course (INSAT).

## Objective

Build an end-to-end GitOps pipeline: the Git repository is the source of
truth for the state of the Kubernetes cluster, and ArgoCD automatically
synchronizes the cluster with what is declared in the repository.

## How it works

1. A change to the application code is pushed to `app/`.
2. The CI (GitHub Actions) tests the code, builds the Docker image and
   publishes it to GitHub Container Registry, tagged with the commit SHA.
3. The CI updates the image tag in `k8s/` and commits that change.
4. ArgoCD, running inside the cluster, detects the difference between the
   repository and the cluster, then applies the new version.

The CI never accesses the cluster: ArgoCD pulls the desired state from
Git (*pull* model).

## Repository contents

| Directory            | Purpose                                                  |
|----------------------|----------------------------------------------------------|
| `app/`               | Demo application (Python/Flask) and its Dockerfile       |
| `k8s/`               | Kubernetes manifests: desired state, watched by ArgoCD   |
| `argocd/`            | ArgoCD Application definition                            |
| `.github/workflows/` | CI pipeline                                              |

## Tools

Docker, kind (local Kubernetes cluster), kubectl, ArgoCD, GitHub Actions,
GitHub Container Registry.
