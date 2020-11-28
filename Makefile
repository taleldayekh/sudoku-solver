SRC_DIR = server/

fix:
	pipenv run isort $(SRC_DIR)
	pipenv run black $(SRC_DIR)

lint:
	pipenv run pylint --rcfile=setup.cfg $(SRC_DIR)

type-check:
	pipenv run mypy $(SRC_DIR)

test:
	pipenv run pytest --cov=server/

