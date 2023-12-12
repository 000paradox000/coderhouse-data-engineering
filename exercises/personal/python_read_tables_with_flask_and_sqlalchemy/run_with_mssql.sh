#!/usr/bin/env bash

docker compose \
  -f ../../../docker/docker-compose.yaml \
  exec -ti flask bash -c \
  "python /opt/exercises/personal/python_read_tables_with_flask_and_sqlalchemy/run.py --engine=mssql"
