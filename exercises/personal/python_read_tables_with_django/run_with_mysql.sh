#!/usr/bin/env bash

docker compose \
  -f ../../../docker/docker-compose.yaml \
  exec -ti django bash -c \
  "python /opt/exercises/personal/python_read_tables_with_fastapi_and_sqlalchemy/run.py --engine=mysql"
