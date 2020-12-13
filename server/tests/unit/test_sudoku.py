from server.app_sudoku.domain.sudoku import (
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
    solve_sudoku,
    sudoku_to_list,
    validate_sudoku_input,
)
from server.tests.utils.mock_data import (
    VALID_SUDOKU,
    VALID_SUDOKU_HARD,
    VALID_SUDOKU_HARD_SOLVED,
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
    sudoku = VALID_SUDOKU
    sudoku[0] = 1
    sudoku[1] = 1
    solved_sudoku = solve_sudoku(sudoku)
    assert len(solved_sudoku) == 0


def test_can_solve_hard_sudoku() -> None:
    solved_sudoku = solve_sudoku(VALID_SUDOKU_HARD)
    assert solved_sudoku == VALID_SUDOKU_HARD_SOLVED


def test_sudoku_to_list() -> None:
    assert sudoku_to_list({0: "3", 1: "2"}) == [3, 2]
