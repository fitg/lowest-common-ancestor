unit-test:
	poetry run pytest -vv .

lint:
	poetry run flake8

black:
	poetry run black -v .

mypy:
	poetry run mypy --strict .

run:
	poetry run execute 1232 21122

all: unit-test black mypy lint run
