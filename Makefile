build-prod:
	docker compose -f docker-compose-prod.yaml build --no-cache

upd:
	docker compose -f docker-compose-prod.yaml up -d

up:
	docker compose -f docker-compose-prod.yaml up

shell-prod:
	docker compose -f docker-compose-prod.yaml exec web bash

makemigrations:
	docker compose -f docker-compose-prod.yaml exec web su -c "python manage.py makemigrations --settings=core.settings.production"

migrate:
	docker compose -f docker-compose-prod.yaml exec web su -c "python manage.py migrate --settings=core.settings.production"

destroy:
	docker compose -f docker-compose-prod.yaml down

createsuperuser:
	docker compose -f docker-compose-prod.yaml exec web su -c "python manage.py createsuperuser --settings=core.settings.production"