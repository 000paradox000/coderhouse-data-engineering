#!/usr/bin/env bash

docker compose \
  -f ../../../../docker/docker-compose.yaml \
  exec -ti python bash -c \
  "python /opt/exercises/semana1/python/ejercicio_5/main.py"
