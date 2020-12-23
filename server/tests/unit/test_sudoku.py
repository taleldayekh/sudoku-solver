from server.app_sudoku.domain.sudoku import Sudoku
from server.app_sudoku.domain.sudoku_utils import (
    NCOLS,
    NROWS,
    PEERS,
    SQUARES,
    UNITS,
    get_box,
    get_box_number,
    get_column,
    get_column_number,
    get_row,
    get_row_number,
    has_unique_solution,
    solve_sudoku,
    sudoku_to_list,
    validate_sudoku_input,
    verify_solution,
)
from server.tests.utils.mock_data import (
    INVALID_SUDOKU,
    UNSOLVABLE_SUDOKU,
    VALID_SUDOKU,
    VALID_SUDOKU_HARD,
    VALID_SUDOKU_HARD_SOLVED,
    VALID_SUDOKU_NON_UNIQUE,
    VALID_SUDOKU_SOLVED,
)


def test_dimensions() -> None:
    assert NCOLS == 9
    assert NROWS == 9


def test_squares() -> None:
    assert SQUARES == list(range(NCOLS * NROWS))


def test_units() -> None:
    index = 4
    unitlist = UNITS[index]
    assert unitlist[0] == get_row(SQUARES, get_row_number(index))
    assert unitlist[1] == get_column(SQUARES, get_column_number(index))
    assert unitlist[2] == get_box(SQUARES, get_box_number(index))


def test_peers() -> None:
    index = 7
    peers = PEERS[index]
    temp = set()
    for unit in UNITS[index]:
        for square in unit:
            temp.add(square)
    temp.remove(index)
    assert list(temp) == peers


def test_get_row() -> None:
    row_test = get_row(list(range(NCOLS * NROWS)), 7)
    row = [63, 64, 65, 66, 67, 68, 69, 70, 71]
    assert row_test == row


def test_get_column() -> None:
    col_test = get_column(list(range(NCOLS * NROWS)), 4)
    col = [4, 13, 22, 31, 40, 49, 58, 67, 76]
    assert col_test == col


def test_get_box() -> None:
    box_test = get_box(list(range(NCOLS * NROWS)), 5)
    box = [33, 34, 35, 42, 43, 44, 51, 52, 53]
    assert box_test == box


def test_can_validate_sudoku_input() -> None:
    test_list = [1 for i in range(81)]
    assert validate_sudoku_input(test_list)


def test_cannot_validate_sudoku_input() -> None:
    test_list = [0 for i in range(81)]
    test_list[0] = -1
    assert not validate_sudoku_input(test_list)
    test_list[0] = 10
    assert not validate_sudoku_input(test_list)
    test_list[0] = "a"  # type: ignore
    assert not validate_sudoku_input(test_list)
    assert not validate_sudoku_input([1, 2])


def test_can_solve_simple_sudoku() -> None:
    solved_sudoku = solve_sudoku(VALID_SUDOKU)
    assert solved_sudoku == VALID_SUDOKU_SOLVED


def test_incorrect_sudoku_returns_empty_list() -> None:
    sudoku = INVALID_SUDOKU
    solved_sudoku = solve_sudoku(sudoku)
    assert len(solved_sudoku) == 0


def test_can_solve_hard_sudoku() -> None:
    solved_sudoku = solve_sudoku(VALID_SUDOKU_HARD)
    assert solved_sudoku == VALID_SUDOKU_HARD_SOLVED


def test_sudoku_to_list() -> None:
    assert sudoku_to_list({0: "3", 1: "2"}) == [3, 2]


def test_sudoku_object_incorrect_input() -> None:
    sudoku = [1, 2, 3]
    S = Sudoku(sudoku)
    assert S.input == sudoku
    assert not S.is_valid
    assert not S.solved
    assert not S.is_solvable
    assert not S.hint


def test_sudoku_object_unsolvable_input() -> None:
    S = Sudoku(UNSOLVABLE_SUDOKU)
    assert S.input == UNSOLVABLE_SUDOKU
    assert S.is_valid
    assert not S.solved
    assert not S.is_solvable
    assert not S.hint


def test_sudoku_object_correct_input() -> None:
    sudoku = VALID_SUDOKU_HARD
    S = Sudoku(sudoku)
    assert S.input == sudoku
    assert S.is_valid
    assert S.solved == VALID_SUDOKU_HARD_SOLVED
    assert S.is_solvable
    hint = S.hint
    assert VALID_SUDOKU_HARD_SOLVED[hint[0]] == hint[1]


def test_verify_solution() -> None:
    assert verify_solution(VALID_SUDOKU_SOLVED)
    assert not verify_solution(VALID_SUDOKU)


def test_has_unique_solution() -> None:
    assert has_unique_solution(VALID_SUDOKU_HARD)
    assert not has_unique_solution(VALID_SUDOKU_NON_UNIQUE)
