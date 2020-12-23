from typing import List

from server.app_sudoku.domain.sudoku import Sudoku
from server.app_sudoku.use_cases.post_solve import InvalidSudoku


def get_hint(sudoku_board: List[int]) -> List[int]:
    sudoku = Sudoku(sudoku_board)

    if not sudoku.is_valid:
        raise InvalidSudoku("Not a valid sudoku")
    return sudoku.hint
