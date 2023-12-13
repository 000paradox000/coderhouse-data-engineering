#!/usr/bin/env bash

docker compose \
  -f ../../../docker/docker-compose.yaml \
  exec -ti fastapi bash -c \
  "python /opt/exercises/personal/python_read_tables_with_django/manage.py runserver 0.0.0.0:9600"
