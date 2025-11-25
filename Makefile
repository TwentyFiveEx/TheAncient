.PHONY: build push build-test test clean

IMAGE_TEST := theancient-test
IMAGE_NAME := theburb/theancient
IMAGE_TAG := $(shell git rev-parse --short=7 HEAD)

LOG_LEVEL := "INFO"

ifdef $$LOG_LEVEL
	LOG_LEVEL := "$${LOG_LEVEL}"
endif


ifneq (,$(wildcard $(CURDIR)/.docker))
	DOCKER_CONF := $(CURDIR)/.docker
else
	DOCKER_CONF := $(HOME)/.docker
endif

# --secret id=steamtoken,env=STEAM_TOKEN --secret id=discordtoken,env=ANCIENT_TOKEN

build:
	@docker build -t $(IMAGE_NAME):latest -f dockerfiles/Dockerfile .
	@docker tag $(IMAGE_NAME):latest $(IMAGE_NAME):$(IMAGE_TAG)

push:
	@docker --config=$(DOCKER_CONF) push $(IMAGE_NAME):latest
	@docker --config=$(DOCKER_CONF) push $(IMAGE_NAME):$(IMAGE_TAG)

build-test:
	@docker build -t $(IMAGE_TEST) -f dockerfiles/Dockerfile.test .

test: build-test
@docker run --secret id=steamtoken,env=STEAM_TOKEN --secret id=discordtoken,env=ANCIENT_TOKEN --rm $(IMAGE_TEST)

debug-test:
@docker run -it --secret id=steamtoken,env=STEAM_TOKEN --secret id=discordtoken,env=ANCIENT_TOKEN -e LOG_LEVEL=$(LOG_LEVEL) --rm $(IMAGE_TEST) bash

debug-build:
@docker run -it --secret id=steamtoken,env=STEAM_TOKEN --secret id=discordtoken,env=ANCIENT_TOKEN -e LOG_LEVEL=$(LOG_LEVEL) --rm $(IMAGE_NAME):$(IMAGE_TAG) bash

run:
@docker run -it --secret id=steamtoken,env=STEAM_TOKEN --secret id=discordtoken,env=ANCIENT_TOKEN -e LOG_LEVEL=$(LOG_LEVEL) --rm $(IMAGE_NAME):$(IMAGE_TAG)

clean:
	@rm -rf .tox .eggs theancient.egg-info build .pytest_cache
	@find . -name "__pycache__" -type d -print0 | xargs -0 rm -rf
	@find . -name "*.pyc" -delete
