from typing import List

from server.app_sudoku.domain.sudoku_generator_model import SudokuGenerator


def generate_sudoku() -> List[int]:
    generator = SudokuGenerator()
    return generator.easy
