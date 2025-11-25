#!/bin/sh

./manual-build/docker-login.sh && ./manual-build/build.sh && ./manual-build/push.sh
