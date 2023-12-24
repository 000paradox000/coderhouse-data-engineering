#!/usr/bin/env bash

docker compose \
  -f ../../../docker/docker-compose.yaml \
  exec -ti python bash -c \
  "sh /opt/exercises/personal/describe_coderhouse_s3_bucket/entrypoint.sh"
