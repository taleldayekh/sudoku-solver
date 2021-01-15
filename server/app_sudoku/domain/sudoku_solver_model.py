import random
from typing import List

from server.app_sudoku.domain.sudoku_base_model import SudokuBase


class SudokuSolver(SudokuBase):
    def __init__(self, sudoku: List[int]):
        self.sudoku = sudoku

    @property
    def _solve_sudoku(self) -> List[int]:
        parsed_sudoku = self.parse_board(self.sudoku)

        if not parsed_sudoku:
            return []

        solved_sudoku = self.search(parsed_sudoku)

        if not solved_sudoku:
            return []

        solved_sudoku_list = self.sudoku_to_list(solved_sudoku)
        return solved_sudoku_list if self.verify_solution(solved_sudoku_list) else []

    @property
    def _get_hint(self) -> List[int]:
        solved_sudoku = self._solve_sudoku

        if not solved_sudoku:
            return []

        new_squares = []
        for index, square in enumerate(self.sudoku):
            if square == 0:
                new_squares.append([index, solved_sudoku[index]])

        if not new_squares:
            return []

        return random.choice(new_squares)

    @property
    def is_valid(self) -> bool:
        return bool(self.validate_sudoku_input(self.sudoku))

    @property
    def solution(self) -> List[int]:
        return self._solve_sudoku

    @property
    def is_solvable(self) -> bool:
        return bool(self.solution)

    @property
    def hint(self) -> List[int]:
        return self._get_hint

    @property
    def verify(self) -> bool:
        return self.verify_solution(self.sudoku)
