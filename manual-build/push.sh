#!/bin/sh

DOCKER_CONF="${PWD}/.docker"
IMAGE_TAG=$(shell git rev-parse --short=7 HEAD)
IMAGE_NAME="theburb/theancient"
docker --config="${DOCKER_CONF}" push "${IMAGE_NAME}:latest"
docker --config="${DOCKER_CONF}" push "${IMAGE_NAME}:${IMAGE_TAG}"

