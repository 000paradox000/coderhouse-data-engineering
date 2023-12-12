#!/usr/bin/env bash

docker compose \
  -f ../../../docker/docker-compose.yaml \
  exec -ti python bash -c \
  "python /opt/exercises/personal/python_read_tables_without_orm/main.py"
