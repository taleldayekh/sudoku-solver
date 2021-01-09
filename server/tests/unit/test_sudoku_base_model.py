# pylint: disable=W0201
from server.app_sudoku.domain.sudoku_base_model import SudokuBase
from server.tests.utils.mock_data import (
    INVALID_SUDOKU,
    VALID_SUDOKU,
    VALID_SUDOKU_SOLVED,
)


class TestSudokuBase:
    def setup_class(self) -> None:
        self.sudoku_base = SudokuBase()
        self.sudoku_input = [1 for i in range(81)]

    def test_can_validate_sudoku_input(self) -> None:
        valid_sudoku_input = self.sudoku_base.validate_sudoku_input(self.sudoku_input)
        assert bool(valid_sudoku_input)

    def test_cannot_validate_invalid_sudoku_input(self) -> None:
        self.sudoku_input[0] = -1
        assert not self.sudoku_base.validate_sudoku_input(self.sudoku_input)

        self.sudoku_input[0] = 10
        assert not self.sudoku_base.validate_sudoku_input(self.sudoku_input)

        self.sudoku_input[0] = "a"  # type: ignore
        assert not self.sudoku_base.validate_sudoku_input(self.sudoku_input)

        self.sudoku_input = [1, 2]
        assert not self.sudoku_base.validate_sudoku_input(self.sudoku_input)

    def test_can_verify_sudoku_solution(self) -> None:
        assert self.sudoku_base.verify_solution(VALID_SUDOKU_SOLVED)

    def test_cannot_verify_valid_sudoku_solution(self) -> None:
        assert not self.sudoku_base.verify_solution(VALID_SUDOKU)

    def test_cannot_verify_invalid_sudoku_solution(self) -> None:
        assert not self.sudoku_base.verify_solution(INVALID_SUDOKU)  # type: ignore

    def test_sudoku_to_list(self) -> None:
        sudoku = {0: "3", 1: "2"}
        assert self.sudoku_base.sudoku_to_list(sudoku)
