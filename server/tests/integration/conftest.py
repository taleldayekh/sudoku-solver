import pytest

# TODO: Figure out if there is a better/correct way to access and type "FixtureRequest"
from _pytest.fixtures import FixtureRequest

from server import create_app


@pytest.fixture(scope="class")
def api_server(request: FixtureRequest) -> None:
    app = create_app()
    app.config["TESTING"] = True
    request.cls.api = app.test_client()
