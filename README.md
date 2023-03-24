**Technologies used** :

1. Backend: [Django](https://djangoproject.com/)
3. Deployment: Digital Ocean

## Before run this project?

Before try to running this project, please clone the repository on your local system. Afterwards, go to your local storage and run this command

- `pip install poetry`
- `poetry install`

#### Automation Documentation

| **Command**                | **Description**                           | **modes** |
| :------------------------------- | ----------------------------------------------- | --------------- |
| `make build-prod && make upd ` | deploy to production server                     | production      |
| `make migrations`              | running make migrations on server via docker    | production      |
| `make migrate`                 | running migrate on server via docker            | production      |
| `make up`                      | implement migrations to database                | production      |
| `make destroy`                 | destroy docker container on server             | production      |
| `make up-prod`                 | up django project on production non daemon mode | production      |
| `make createsuperuser`         | create superuser on server side                 | production      |
| `make shell-prod`              | opening django shell on server side             | production      |

## Environtment

make a file `.env` and then copy `.env.example` to `.env`

#### Production Environtment

production environment with nginx web service support (only running on docker)

| **Env Variables** | **Sample Value** | **Description**                   |
| ----------------------- | ---------------------- | --------------------------------------- |
| `APP_IP`              | 0.0.0.0                | Main Applications IP                    |
| `APP_PORT`            | 8000                   | main django app port                    |
| `DB_NAME`             | db_postgres            | postgres database name                  |
| `DB_USER`             | user                   | database user                           |
| `DB_PWD`              | passwd                 | database password                       |
| `DB_PORT`             | 5432                   | database port                           |
| `DB_HOST`             | db                     | database host                           |
| `SECRET_KEY`          | pleasereplacethis      | Django secret key                       |
| `DEBUG`               | True                   | Django debug mode on docker development |
| `NGINX_PORT`          | 1338                   | nginx port for production               |
| `HTTP_PORT`           | 80                     | http port for browser access            |
