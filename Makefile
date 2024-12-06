-include .env

default: help

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: ## Build the app.
	docker compose build

pytest: ## Test the app.
	docker compose run app bash -c 'poetry run pytest'

pylint: ## Lint the app.
	docker compose run app bash -c 'poetry run python manage.py pylint'
