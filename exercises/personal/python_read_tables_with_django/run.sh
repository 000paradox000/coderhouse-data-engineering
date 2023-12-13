#!/usr/bin/env bash

docker compose \
  -f ../../../docker/docker-compose.yaml \
  exec -ti django bash -c \
  "sh /opt/exercises/personal/python_read_tables_with_django/entrypoint.sh"
