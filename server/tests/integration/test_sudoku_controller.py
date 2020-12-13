# pylint: disable=E1101
# mypy: ignore-errors
# TODO: Understand how to type the api attribute from the fixture
import json

import pytest

from server.tests.utils.mock_data import INVALID_SUDOKU, VALID_SUDOKU

REQUEST_HEADERS = {"Content-Type": "application/json"}
VALIDATE_ENDPOINT = "/api/v1/sudoku/validate"


@pytest.mark.usefixtures("api_server")
class TestSudokuPOST:
    def test_valid_sudoku_returns_200(self) -> None:
        res = self.api.post(
            VALIDATE_ENDPOINT, data=json.dumps(VALID_SUDOKU), headers=REQUEST_HEADERS
        )

        assert res.status_code == 200

    def test_invalid_sudoku_returns_400(self) -> None:
        res = self.api.post(
            VALIDATE_ENDPOINT, data=json.dumps(INVALID_SUDOKU), headers=REQUEST_HEADERS
        )

        assert res.status_code == 400
