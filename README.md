# FastAPI Heart Disease API — Dockerized

This project exposes a FastAPI application that predicts heart disease using a pre-trained model (`heart_disease_model.pkl`). The repository already includes a local Python virtualenv for development; the instructions below explain how to build and run the app in Docker.

Files added for Docker:
- `Dockerfile` — builds a minimal image and runs Uvicorn on port 80
- `.dockerignore` — keeps unwanted files out of the image
- `docker-compose.yml` — convenience file mapping host 8000 -> container 80

Quick commands (PowerShell):

Build the Docker image:

```powershell
docker build -t fastapi-heart-app .
```

Run with Docker (port 8000 on host -> 80 in container):

```powershell
docker run --rm -p 8000:80 fastapi-heart-app
```

Or use Docker Compose:

```powershell
docker-compose up --build
```

Verify the service is running:

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/health | Select-Object -ExpandProperty Content
```

Notes and tips:
- The Dockerfile installs packages from `requirements.txt`. If you need to pin exact versions for reproducible builds, update `requirements.txt` accordingly.
- The pre-trained model file `heart_disease_model.pkl` must be present in the project root (it is included in the repository). When building the image, the file will be copied into `/app` and available to `main.py`.
- For production use, consider using an ASGI process manager (gunicorn + uvicorn workers) and non-root user in the image.
