#!/bin/sh

IMAGE_TAG="$(git rev-parse --short=7 HEAD)"
IMAGE_NAME="theburb/theancient"
docker build -t "${IMAGE_NAME}:latest" -f dockerfiles/Dockerfile .
docker tag "${IMAGE_NAME}:latest" "${IMAGE_NAME}:${IMAGE_TAG}"
