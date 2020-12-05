import json
from typing import List

NROWS = 9
NCOLS = 9


def write_to_file(board: List[int], filename: str) -> None:
    with open(filename, "w") as outfile:
        json.dump(board, outfile)


def read_from_file(filename: str) -> List[int]:
    with open(filename, "r") as infile:
        return json.load(infile)


def print_sudoku_simple(board: List[int]) -> None:
    for row in range(NROWS):
        for col in range(NCOLS):
            num = board[row * NROWS + col]
            print(num, end=" ")
        print(" ")


def print_sudoku(board: List[int]) -> None:
    divider = "|———————|———————|———————|"
    for row in range(NROWS):
        if row % 3 == 0:
            print(divider)
        for col in range(NCOLS):
            if col % 3 == 0:
                print("| ", end="")
            num = board[row * NROWS + col]
            if num > 0:
                print(num, end=" ")
            else:
                print(" ", end=" ")
        print("|")
    print(divider)


# 0-8 is row 0 , 9-17 row 1 etc.
def get_row_number(index: int) -> int:
    return index // NROWS


# 0,9,18,27,36,45,54,63,72 is column 0 etc.
def get_column_number(index: int) -> int:
    return index % NCOLS


# rows 0-2 and column 0-2 is box 1, rows 0-2 and column 3-5 is box 2 etc.
def get_box_number(index: int) -> int:
    return 3 * (get_row_number(index) // 3) + get_column_number(index) // 3


def get_row(board: List[int], row: int) -> List[int]:
    return [board[row * NROWS + i] for i in range(NCOLS)]


def get_column(board: List[int], column: int) -> List[int]:
    return [board[column + NROWS * i] for i in range(NROWS)]


def get_box(board: List[int], box: int) -> List[int]:
    boxlist = []
    for i in range(NROWS * NCOLS):
        if get_box_number(i) == box:
            boxlist.append(board[i])
    return boxlist


def validate_region(region: List[int]) -> bool:
    numbers_unique = set()
    for num in region:
        if num > 0:
            if num in numbers_unique:
                return False
            numbers_unique.add(num)
    return True


def validate_row(board: List[int], row_index: int) -> bool:
    row = get_row(board, row_index)
    return validate_region(row)


def validate_column(board: List[int], column_index: int) -> bool:
    column = get_column(board, column_index)
    return validate_region(column)


def validate_box(board: List[int], box_index: int) -> bool:
    box = get_box(board, box_index)
    return validate_region(box)


def validate_list_entries(board: List[int]) -> bool:
    # Check size
    if len(board) != NROWS * NCOLS:
        return False
    # check all ints
    for num in board:
        if isinstance(num, int):
            continue
        return False
    # check number range
    if max(board) > 9 or min(board) < 0:
        return False
    return True


def validate_sudoku(board: List[int]) -> bool:
    if not validate_list_entries(board):
        return False
    # validate all regions
    for row in range(NROWS):
        if not validate_row(board, i):
            return False
        if not validate_column(board, i):
            return False
        if not validate_box(board, i):
            return False
    return True


if __name__ == "__main__":
    S = read_from_file("example_sudoku.json")
    print_sudoku(S)
    print(validate_sudoku(S))
    S[0] = 1
    S[1] = 1
    print_sudoku(S)
    print(validate_sudoku(S))

    S_solved = read_from_file("example_sudoku_solved.json")
    print_sudoku(S_solved)
    print(validate_sudoku(S_solved))
