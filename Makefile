.DEFAULT_GOAL := help
.PHONY: coverage deps help lint test clear-cache

coverage:  ## Run tests with coverage
	poetry run coverage erase
	poetry run coverage run --include=fido/* -m pytest -ra
	poetry run coverage report -m

deps:  ## Install dependencies
	poetry install

lint:  ## Lint and static-check
	poetry run flake8 fido
	poetry run pylint fido
	poetry run mypy fido

test:  ## Run tests
	poetry run pytest -ra

clear-cache:  ## Clear local fido cache
	rm -rf .fido/* && mkdir .fido
