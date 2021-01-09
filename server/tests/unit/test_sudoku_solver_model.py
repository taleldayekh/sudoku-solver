from server.app_sudoku.domain.sudoku_solver_model import SudokuSolver
from server.tests.utils.mock_data import (
    INVALID_SUDOKU,
    UNSOLVABLE_SUDOKU,
    VALID_SUDOKU,
    VALID_SUDOKU_HARD,
    VALID_SUDOKU_HARD_SOLVED,
    VALID_SUDOKU_SOLVED,
)


def test_can_solve_simple_sudoku() -> None:
    sudoku_solution = SudokuSolver(VALID_SUDOKU).solution
    assert sudoku_solution == VALID_SUDOKU_SOLVED


def test_can_solve_hard_sudoku() -> None:
    sudoku_solution = SudokuSolver(VALID_SUDOKU_HARD).solution
    assert sudoku_solution == VALID_SUDOKU_HARD_SOLVED


def test_solution_returns_empty_list_on_incorrect_input() -> None:
    invalid_sudoku = SudokuSolver(INVALID_SUDOKU).solution  # type: ignore
    assert invalid_sudoku == []


def test_unsolvable_sudoku() -> None:
    unsolvable_sudoku = SudokuSolver(UNSOLVABLE_SUDOKU)

    assert unsolvable_sudoku.is_valid
    assert not unsolvable_sudoku.solution
    assert not unsolvable_sudoku.is_solvable
    assert not unsolvable_sudoku.hint


def test_correct_sudoku() -> None:
    correct_sudoku = SudokuSolver(VALID_SUDOKU_HARD)

    assert correct_sudoku.is_valid
    assert correct_sudoku.solution == VALID_SUDOKU_HARD_SOLVED
    assert correct_sudoku.is_solvable
    assert correct_sudoku.hint


def test_incorrect_sudoku() -> None:
    incorrect_sudoku = SudokuSolver([1, 2, 3])

    assert not incorrect_sudoku.is_valid
    assert not incorrect_sudoku.solution
    assert not incorrect_sudoku.is_solvable
    assert not incorrect_sudoku.hint


def test_can_provide_sudoku_hint() -> None:
    sudoku = SudokuSolver(VALID_SUDOKU_HARD)
    hint = sudoku.hint
    assert VALID_SUDOKU_HARD_SOLVED[hint[0]] == hint[1]


def test_cannot_provide_sudoku_hint() -> None:
    sudoku = SudokuSolver(VALID_SUDOKU_SOLVED)
    hint = sudoku.hint
    assert not hint
