up:
	sh mysql/bash_scripts/init.sh
	sh s3/bash_scripts/init.sh
	docker compose up --build

down:
	docker compose down

list-bucket-coderhouse:
	aws --endpoint-url=http://localhost:4566 s3 ls coderhouse
