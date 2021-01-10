# pylint: disable=W0212
from server.app_sudoku.domain.sudoku_generator_model import SudokuGenerator
from server.app_sudoku.domain.sudoku_solver_model import SudokuSolver
from server.tests.utils.mock_data import (
    INVALID_SUDOKU,
    UNSOLVABLE_SUDOKU,
    VALID_SUDOKU_HARD,
    VALID_SUDOKU_NON_UNIQUE,
)


def test_sudoku_has_unique_solution() -> None:
    assert SudokuGenerator()._unique_solution(VALID_SUDOKU_HARD)


def test_sudoku_has_no_unique_solution() -> None:
    assert not SudokuGenerator()._unique_solution(INVALID_SUDOKU)  # type: ignore
    assert not SudokuGenerator()._unique_solution(UNSOLVABLE_SUDOKU)
    assert not SudokuGenerator()._unique_solution(VALID_SUDOKU_NON_UNIQUE)


def test_can_generate_easy_sudoku() -> None:
    easy_sudoku = SudokuGenerator().easy
    sudoku = SudokuSolver(easy_sudoku)

    assert sudoku.is_valid
    assert sudoku.solution


def test_can_generate_hard_sudoku() -> None:
    hard_sudoku = SudokuGenerator().hard
    sudoku = SudokuSolver(hard_sudoku)

    assert sudoku.is_valid
    assert sudoku.solution
