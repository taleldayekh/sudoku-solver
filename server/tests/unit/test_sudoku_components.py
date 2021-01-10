from server.app_sudoku.domain import sudoku_components

NUM_OF_SQUARES = sudoku_components.NUM_OF_SQUARES


def test_can_get_row() -> None:
    sudoku_row = sudoku_components.get_row(list(range(NUM_OF_SQUARES)), 7)
    assert sudoku_row == [63, 64, 65, 66, 67, 68, 69, 70, 71]


def test_can_get_col() -> None:
    sudoku_col = sudoku_components.get_col(list(range(NUM_OF_SQUARES)), 4)
    assert sudoku_col == [4, 13, 22, 31, 40, 49, 58, 67, 76]


def test_can_get_box() -> None:
    sudoku_box = sudoku_components.get_box(list(range(NUM_OF_SQUARES)), 5)
    assert sudoku_box == [33, 34, 35, 42, 43, 44, 51, 52, 53]


def test_can_generate_units() -> None:
    # TODO: Add test, the previous test was not testing the function
    pass


def test_can_generate_peers() -> None:
    # TODO: Add test, the previous test was not testing the function
    pass
