from typing import List

from server.app_sudoku.domain.sudoku_solver_model import SudokuSolver
from server.app_sudoku.use_cases.post_solve import InvalidSudoku


def verify_sudoku(sudoku_board: List[int]) -> bool:
    sudoku = SudokuSolver(sudoku_board)

    if not sudoku.is_valid:
        raise InvalidSudoku("Not a valid sudoku")
    return sudoku.verify
