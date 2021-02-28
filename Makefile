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
	pipenv run python3 -m pytest --cov-report=xml --cov-report term --cov=. ./$(SRC_DIR)/tests/unit -v -s

test-e2e:
	pipenv run python3 -m pytest --cov-report=xml --cov-report term --cov=. ./$(SRC_DIR)/tests/e2e -v -s
