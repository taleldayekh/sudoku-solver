from typing import List

from server.app_sudoku.domain.sudoku import SudokuGenerator


def generate_sudoku() -> List[int]:
    generator = SudokuGenerator()
    return generator.generate_easy
