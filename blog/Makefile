# Variables
DOCKER_COMPOSE = docker-compose -f docker-compose.yml --env-file .env.prod

.PHONY: up down build restart logs shell migrate makemigrations collectstatic

up:
	$(DOCKER_COMPOSE) up -d --build

down:
	$(DOCKER_COMPOSE) down

build:
	$(DOCKER_COMPOSE) build

restart:
	$(DOCKER_COMPOSE) restart

logs:
	$(DOCKER_COMPOSE) logs -f

shell:
	$(DOCKER_COMPOSE) exec web sh

migrate:
	$(DOCKER_COMPOSE) exec web python manage.py migrate

makemigrations:
	$(DOCKER_COMPOSE) exec web python manage.py makemigrations

collectstatic:
	$(DOCKER_COMPOSE) exec web python manage.py collectstatic --noinput
