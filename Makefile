-include .env

default: help

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: ## Build the app.
	docker compose build --remove-orphans

pytest: ## Test the app.
	docker compose run app bash -c 'poetry run python manage.py pytest'

pylint: ## Lint the app.
	docker compose run app bash -c 'poetry run python manage.py pylint'

mypy: ## Static analysis on the app.
	docker compose run app bash -c 'poetry run python manage.py mypy'

checks: pylint mypy pytest ## Run all checks (pylint, mypy, pytest) against the project.

clean: ## Clean up the containerspace.
	docker compose down --remove-orphans
