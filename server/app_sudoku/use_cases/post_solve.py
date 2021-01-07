from typing import List

from server.app_sudoku.domain.sudoku_solver_model import SudokuSolver


class InvalidSudoku(Exception):
    pass


def solve_sudoku(sudoku_board: List[int]) -> List[int]:
    sudoku = SudokuSolver(sudoku_board)

    if not sudoku.is_valid:
        raise InvalidSudoku("Not a valid sudoku")
    return sudoku.solution
