from typing import List

from server.app_sudoku.domain.model import validate_sudoku


def post_validate(sudoku_board: List[int]) -> bool:
    return validate_sudoku(sudoku_board)
