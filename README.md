# CODERHOUSE Data Engineering

URL: https://plataforma-beta.coderhouse.com/cursos/56025/data-engineering-flex

Teachers:

- Juan Pablo Visbeek
- Javier Poblete

## Containers

To satrt the container you can do 

```shell
cd docker
docker compose up --build
```

### MySQL Database

| Setting       | Value      |
|---------------|------------|
| Host          | db_mysql   |
| User          | coderhouse |
| Password      | coderhouse |
| Database name | coderhouse |
| Port          | 3308       |

### PostgreSQL Database

| Setting       | Value       |
|---------------|-------------|
| Host          | db_postgres |
| User          | coderhouse  |
| Password      | coderhouse  |
| Database name | coderhouse  |
| Port          | 5438        |

### Microsoft SQL Server Database

| Setting       | Value      |
|---------------|------------|
| Host          | db_mssql   |
| User          | coderhouse |
| Password      | C0d3rhous3 |
| Database name | coderhouse |
| Port          | 1438       |

### phpmyadmin MySQL database web client

| Setting       | Value                   |
|---------------|-------------------------|
| URL           | http://localhost:8501   |
| User          | coderhouse              |
| Password      | C0d3rhous3              |

### pgadmin PostgreSQL database web client

| Setting       | Value                 |
|---------------|-----------------------|
| URL           | http://localhost:8502 |
| User          | admin@coderhouse.com  |
| Password      | coderhouse            |

### sqlpad Microsoft SQL Server database web client

| Setting       | Value                 |
|---------------|-----------------------|
| URL           | http://localhost:8503 |
| User          | admin@coderhouse.com  |
| Password      | C0d3rhous3            |

### jupyterlab

| Setting       | Value                 |
|---------------|-----------------------|
| URL           | http://localhost:8504 |

### python

| Setting                   | Value                                                 |
|---------------------------|-------------------------------------------------------|
| Version                   | 3.11                                                  |
| Execute a python script   | docker compose exec -ti python bash -c "python PATH"  |

### Flask

| Setting       | Value      |
|---------------|------------|
| Port          | 8505       |

### Fastapi

| Setting       | Value |
|---------------|-------|
| Port          | 8506  |

### Django

| Setting       | Value |
|---------------|-------|
| Port          | 8507  |

## Exercises

### Personal

- Read DB tables with Django
- Read DB tables with FastAPI and SQLAlchemy
- Read DB tables with Flask and SQLAlchemy
- Read DB tables with python withot any ORM

## Links

- [Como Crear BASE DE DATOS en SQL SERVER Desde Cero 😉](https://www.youtube.com/watch?v=fyvEhDgKl7E)
- [Introducción a las redes en docker. Enlazando contenedores docker](https://www.josedomingo.org/pledin/2020/02/redes-en-docker/)