# FastAPI Docker EC2 CI/CD

A simple DevOps project demonstrating containerization and automated deployment of a FastAPI application to AWS EC2.

## Architecture

```text
GitHub
  ↓
GitHub Actions
  ↓
Docker Build
  ↓
Amazon ECR
  ↓
AWS Systems Manager (SSM)
  ↓
EC2
  ↓
Docker Container
  ↓
FastAPI
```

## Tech Stack

* Python / FastAPI
* Docker
* AWS EC2
* Amazon ECR
* AWS Systems Manager (SSM)
* GitHub Actions

## Deployment Flow

1. Checkout source code.
2. Build the Docker image.
3. Authenticate with Amazon ECR.
4. Tag and push the image to ECR.
5. Trigger deployment on EC2 using SSM.
6. Pull the latest image from ECR.
7. Replace the existing container.
8. Run the FastAPI container.

## Manual Docker Commands

```bash
# Build
docker build -t fastapi-image .

# Tag
docker tag fastapi-image:latest <ECR_URI>:latest

# Push
docker push <ECR_URI>:latest

# Pull
docker pull <ECR_URI>:latest

# Run
docker run -d --name fastapi-app -p 8000:5000 <ECR_URI>:latest
```

## Application

Once deployed:

```text
http://<EC2-PUBLIC-IP>:8000
```

Health endpoint:

```text
http://<EC2-PUBLIC-IP>:8000/health
```
