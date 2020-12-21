# pylint: disable=E1101
# mypy: ignore-errors
# TODO: Understand how to type the api attribute from the fixture
import json

import pytest

from server.tests.utils.mock_data import (
    INVALID_SUDOKU,
    UNSOLVABLE_SUDOKU,
    VALID_SUDOKU,
    VALID_SUDOKU_SOLVED,
)

REQUEST_HEADERS = {"Content-Type": "application/json"}
SOLVE_ENDPOINT = "api/v1/sudoku/solve"


@pytest.mark.usefixtures("api_server")
class TestSudokuPOST:
    def test_solvable_sudoku_returns_solved_sudoku(self) -> None:
        res = self.api.post(
            SOLVE_ENDPOINT,
            data=json.dumps({"sudoku": VALID_SUDOKU}),
            headers=REQUEST_HEADERS,
        )
        res_data = json.loads(res.get_data(as_text=True))

        assert res_data["data"] == VALID_SUDOKU_SOLVED
        assert res.status_code == 200

    def test_unsolvable_sudoku_returns_200(self) -> None:
        res = self.api.post(
            SOLVE_ENDPOINT,
            data=json.dumps({"sudoku": UNSOLVABLE_SUDOKU}),
            headers=REQUEST_HEADERS,
        )
        res_data = json.loads(res.get_data(as_text=True))

        assert res_data["data"] == "Sudoku is unsolvable"
        assert res.status_code == 200

    def test_invalid_json_key_returns_400(self) -> None:
        res = self.api.post(
            SOLVE_ENDPOINT,
            data=json.dumps({"not-a-valid-key": VALID_SUDOKU}),
            headers=REQUEST_HEADERS,
        )
        res_data = json.loads(res.get_data(as_text=True))

        assert res_data["error"] == "Invalid JSON key"
        assert res.status_code == 400

    def test_invalid_sudoku_returns_400(self) -> None:
        res = self.api.post(
            SOLVE_ENDPOINT,
            data=json.dumps({"sudoku": INVALID_SUDOKU}),
            headers=REQUEST_HEADERS,
        )
        res_data = json.loads(res.get_data(as_text=True))

        assert res_data["error"] == "Not a valid sudoku"
        assert res.status_code == 400