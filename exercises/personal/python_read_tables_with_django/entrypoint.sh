#!/usr/bin/env bash

cd /opt/exercises/personal/python_read_tables_with_django

rm -Rf coderhouse/db/*.db

python manage.py makemigrations
python manage.py migrate

DJANGO_SUPERUSER_USERNAME="admin"
DJANGO_SUPERUSER_EMAIL="admin@coderhouse.com"
DJANGO_SUPERUSER_PASSWORD="admin"

python manage.py createsuperuser --noinput \
  --username $DJANGO_SUPERUSER_USERNAME \
  --email $DJANGO_SUPERUSER_EMAIL

echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
      user = User.objects.get(username='$DJANGO_SUPERUSER_USERNAME'); \
      user.set_password('$DJANGO_SUPERUSER_PASSWORD'); user.save()" | python manage.py shell

python manage.py runserver 0.0.0.0:9600
