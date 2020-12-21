from typing import List

from server.app_sudoku.domain.sudoku import Sudoku


class InvalidSudoku(Exception):
    pass


def solve_sudoku(sudoku_board: List[int]) -> List[int]:
    sudoku = Sudoku(sudoku_board)

    if not sudoku.is_valid:
        raise InvalidSudoku("Not a valid sudoku")
    return sudoku.solved
