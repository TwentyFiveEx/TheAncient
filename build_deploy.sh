#!/bin/bash

DOCKER_CONF="$PWD/.docker"
mkdir -p "${DOCKER_CONF}"
docker --config "${DOCKER_CONF}" login -u "${DOCKER_USER}" -p "${DOCKER_TOKEN}" 

# build images
make build push
