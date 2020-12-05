from server.sudoku import (
    read_from_file,
    validate_list_entries,
    validate_region,
    validate_sudoku,
)


def test_can_validate_list_entries() -> None:
    test_list = [0 for i in range(81)]
    assert validate_list_entries(test_list)


def test_cannot_validate_list_entries() -> None:
    test_list = [0 for i in range(81)]
    test_list[0] = -1
    assert not validate_list_enries(test_list)
    test_list[0] = 10
    assert not validate_list_enries(test_list)
    test_list[0] = "a"  # type: ignore
    assert not validate_list_enries(test_list)
    assert not validate_list_enries([1, 2])


def test_can_validate_region() -> None:
    region = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert validate_region(region)


def test_cannot_validate_region() -> None:
    region = [9, 9, 3, 4, 5, 6, 7, 8, 1]
    assert not validate_region(region)


def test_can_validate_sudoku() -> None:
    sudoku = read_from_file("server/example_sudoku.json")
    assert validate_sudoku(sudoku)


def test_cannot_validate_sudoku() -> None:
    sudoku = read_from_file("server/example_sudoku.json")
    # incorrect row:
    sudoku[0] = 8
    sudoku[8] = 8
    assert not validate_sudoku(sudoku)
    # incorrect column
    sudoku[8] = 0
    sudoku[63] = 8
    assert not validate_sudoku(sudoku)
    # incorrect box
    sudoku[63] = 0
    sudoku[11] = 8
    assert not validate_sudoku(sudoku)
