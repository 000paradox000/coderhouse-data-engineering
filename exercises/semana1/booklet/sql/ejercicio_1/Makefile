up:
	chmod 0444 config_mysql/custom.cnf
	docker compose up --build

down:
	docker compose down

run-python-with-psycopg2:
	docker compose run -it python_with_psycopg2 python main_mysql.py
	docker compose run -it python_with_psycopg2 python main_postgres.py

run-flask-with-postgres:
	docker compose exec -it flask_with_postgres python main.py

run-fastapi-with-mysql:
	docker compose exec -it fastapi_with_mysql python main.py
