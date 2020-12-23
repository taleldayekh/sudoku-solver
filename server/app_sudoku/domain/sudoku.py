from typing import List

from server.app_sudoku.domain.sudoku_utils import (
    generate_sudoku,
    get_hint,
    solve_sudoku,
    validate_sudoku_input,
)


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

    @property
    def hint(self) -> List[int]:
        return get_hint(self.input, self.solved) if self.is_valid else []


class SudokuGenerator:
    def __init__(self) -> None:
        self.number_of_starting_squares_easy = 32
        self.number_of_starting_squares_hard = 23

    @property
    def generate_easy(self) -> List[int]:
        return generate_sudoku(self.number_of_starting_squares_easy)

    @property
    def generate_hard(self) -> List[int]:
        return generate_sudoku(self.number_of_starting_squares_hard)
