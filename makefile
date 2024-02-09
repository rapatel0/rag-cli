# Makefile for managing Docker builds in a multi-stage setup

# Define default target if no arguments are given to make
.DEFAULT_GOAL := help

# Define variables for docker commands to increase readability
DOCKER_BUILD := docker build
DOCKER_TAG := --tag
DOCKER_FILE := --file
DOCKER_TARGET := --target
DOCKER_RMI := docker rmi

# Use an environment variable to specify the stage
STAGE ?= development

# Dockerfile location
DOCKERFILE := docker/Dockerfile

DATA := ~/repos/data/guidances

# Image name
IMAGE_NAME := rag-cli

# Define phony targets for make
.PHONY: help python-base builder-base development lint test production shell

# Display help for commands
help:
	@echo "Available commands:"
	@echo "  python-base    - Build the python-base image"
	@echo "  builder-base   - Build the builder-base image"
	@echo "  development    - Build the development image"
	@echo "  lint           - Build the lint image"
	@echo "  test           - Build the test image"
	@echo "  production     - Build the production image"

# Build python-base stage
python-base:
	$(DOCKER_BUILD) $(DOCKER_FILE) $(DOCKERFILE) $(DOCKER_TARGET) python-base $(DOCKER_TAG) $(IMAGE_NAME):python-base .

# Build builder-base stage
builder-base:
	$(DOCKER_BUILD) $(DOCKER_FILE) $(DOCKERFILE) $(DOCKER_TARGET) builder-base $(DOCKER_TAG) $(IMAGE_NAME):builder-base .

# Build development stage
development:
	$(DOCKER_BUILD) $(DOCKER_FILE) $(DOCKERFILE) $(DOCKER_TARGET) development $(DOCKER_TAG) $(IMAGE_NAME):development .

# Build lint stage
lint:
	$(DOCKER_BUILD) $(DOCKER_FILE) $(DOCKERFILE) $(DOCKER_TARGET) lint $(DOCKER_TAG) $(IMAGE_NAME):lint .

# Build test stage
test:
	$(DOCKER_BUILD) $(DOCKER_FILE) $(DOCKERFILE) $(DOCKER_TARGET) test $(DOCKER_TAG) $(IMAGE_NAME):test .

# Build production stage
production:
	$(DOCKER_BUILD) $(DOCKER_FILE) $(DOCKERFILE) $(DOCKER_TARGET) production $(DOCKER_TAG) $(IMAGE_NAME):production .

# Clean up built Docker images
clean:
	-@$(DOCKER_RMI) $(IMAGE_NAME):python-base || true
	-@$(DOCKER_RMI) $(IMAGE_NAME):builder-base || true
	-@$(DOCKER_RMI) $(IMAGE_NAME):development || true
	-@$(DOCKER_RMI) $(IMAGE_NAME):lint || true
	-@$(DOCKER_RMI) $(IMAGE_NAME):test || true
	-@$(DOCKER_RMI) $(IMAGE_NAME):production || true


# Conditional logic to set the Docker tag based on the STAGE variable
ifeq ($(STAGE),python-base)
  DOCKER_TAG := python-base
else ifeq ($(STAGE),builder-base)
  DOCKER_TAG := builder-base
else ifeq ($(STAGE),development)
  DOCKER_TAG := development
else ifeq ($(STAGE),lint)
  DOCKER_TAG := lint
else ifeq ($(STAGE),test)
  DOCKER_TAG := test
else ifeq ($(STAGE),production)
  DOCKER_TAG := production
else
  $(error Invalid stage specified)
endif

# Drop into a shell for the specified stage
shell:
	docker run --rm -it \
		-v ${PWD}:/app \
		-v $(DATA):/data \
		--entrypoint /bin/bash \
		$(IMAGE_NAME):$(DOCKER_TAG)