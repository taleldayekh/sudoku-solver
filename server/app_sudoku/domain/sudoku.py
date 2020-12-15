from typing import List

from server.app_sudoku.domain.sudoku_utils import solve_sudoku, validate_sudoku_input


class Sudoku:
    def __init__(self, input_sudoku: List[int]):
        self.input = input_sudoku
        self.input_is_valid = False
        self.sudoku_is_solvable = False
        self.solved_sudoku: List[int] = []
        self.check_input()
        self.solve()
        self.check_if_solvable()

    def check_input(self) -> None:
        if validate_sudoku_input(self.input):
            self.input_is_valid = True

    def solve(self) -> None:
        if self.input_is_valid:
            self.solved_sudoku = solve_sudoku(self.input)

    def check_if_solvable(self) -> None:
        if self.solved_sudoku:
            self.sudoku_is_solvable = True
