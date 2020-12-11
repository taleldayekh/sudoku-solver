from typing import List

from server.app_sudoku.domain.sudoku import validate_sudoku_input


def post_validate(sudoku_board: List[int]) -> bool:
    return validate_sudoku_input(sudoku_board)
