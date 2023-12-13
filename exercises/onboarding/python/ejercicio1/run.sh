#!/usr/bin/env bash

docker compose \
  -f ../../../../docker/docker-compose.yaml \
  exec -ti python bash -c \
  "python /opt/exercises/onboarding/python/ejercicio1/main.py"
