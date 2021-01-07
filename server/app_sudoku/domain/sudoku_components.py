from typing import Dict, List, Tuple

SUDOKU_ROWS = 9
SUDOKU_COLS = 9
SUDOKU_BOARD = SUDOKU_ROWS * SUDOKU_COLS
SQUARES = list(range(SUDOKU_BOARD))


def get_row_number(index: int) -> int:
    """
    Index 0-8 corresponds to sudoku
    row 0, index 9-17 to row 1, etc.
    """
    return index // SUDOKU_ROWS


def get_col_number(index: int) -> int:
    """
    Index 0, 9, 18, 27, 36, 45, 54, 63, 72
    corresponds to sudoku column 0, etc.
    """
    return index % SUDOKU_COLS


def get_box_number(index: int) -> int:
    """
    Rows 0-2 and columns 0-2 corresponds to sudoku
    box 1, rows 0-2 and columns 3-5 to box 2, etc.
    """
    row_number = get_row_number(index)
    col_number = get_col_number(index)

    return 3 * (row_number // 3) + col_number // 3


def get_row(board: List[int], row: int) -> List[int]:
    """
    TODO: Add docstring
    """
    return [board[row * SUDOKU_ROWS + col] for col in range(SUDOKU_COLS)]


def get_col(board: List[int], col: int) -> List[int]:
    """
    TODO: Add docstring
    """
    return [board[col + SUDOKU_ROWS * row] for row in range(SUDOKU_ROWS)]


def get_box(board: List[int], box: int) -> List[int]:
    """
    TODO: Add docstring
    """
    box_list = []

    for index in range(SUDOKU_BOARD):
        if get_box_number(index) == box:
            box_list.append(board[index])

    return box_list


def generate_units_and_peers() -> Tuple[
    Dict[int, List[List[int]]], Dict[int, List[int]]
]:
    units = dict()
    peers = dict()

    for index in range(SUDOKU_BOARD):
        units_list = [
            get_row(SQUARES, get_row_number(index)),
            get_col(SQUARES, get_col_number(index)),
            get_box(SQUARES, get_box_number(index)),
        ]
        units[index] = units_list

        # TODO: Rename temp to something more descriptive
        temp = set()

        for unit in units_list:
            for square in unit:
                temp.add(square)

        temp.remove(index)
        peers_list = list(temp)
        peers[index] = peers_list

    return units, peers


UNITS, PEERS = generate_units_and_peers()
