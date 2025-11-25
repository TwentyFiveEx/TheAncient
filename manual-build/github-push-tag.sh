#!/bin/sh

IMAGE_TAG="$(git rev-parse --short=7 HEAD)"
git tag ${IMAGE_TAG}
git push --tags
