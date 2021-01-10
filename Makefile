SRC_DIR = server/

server-api:
	pipenv run python -m flask run

fix:
	pipenv run isort $(SRC_DIR)
	pipenv run black $(SRC_DIR)

lint:
	pipenv run pylint --rcfile=setup.cfg $(SRC_DIR)

type-check:
	pipenv run mypy $(SRC_DIR)

test-unit:
	pipenv run pytest ./server/tests/unit

test-e2e:
	pipenv run pytest ./server/tests/e2e

test-coverage:
	pipenv run pytest --cov=./server/tests/ --cov-report=xml
