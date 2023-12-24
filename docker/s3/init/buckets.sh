#!/usr/bin/env bash

awslocal s3 mb s3://coderhouse

aws --endpoint-url=http://localhost:4566 s3 sync /opt/data/csv s3://coderhouse