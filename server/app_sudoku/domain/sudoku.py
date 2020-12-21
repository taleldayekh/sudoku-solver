from typing import List

from server.app_sudoku.domain.sudoku_utils import solve_sudoku, validate_sudoku_input


class Sudoku:
    def __init__(self, input_sudoku: List[int]):
        self.input = input_sudoku

    @property
    def is_valid(self) -> bool:
        return bool(validate_sudoku_input(self.input))

    @property
    def is_solvable(self) -> bool:
        return bool(self.solved)

    @property
    def solved(self) -> List[int]:
        return solve_sudoku(self.input) if self.is_valid else []
