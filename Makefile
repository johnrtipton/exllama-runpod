# Variables
IMAGE_NAME ?= johnrtipton/exllama-vicuna-v1.5-16k-gptq-4bit
TAG ?= latest

# Docker build
docker-build:
	@echo "Building Docker image..."
	@docker buildx build --platform=linux/amd64 -t $(IMAGE_NAME) .

docker-login:
    @echo "Logging into Docker Hub..."
    @docker login

docker-push: docker-login
    @echo "Pushing Docker image..."
    @docker push $(IMAGE_NAME)