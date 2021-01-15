import random
from typing import List

from server.app_sudoku.domain.sudoku_components import NUM_OF_SQUARES, SQUARES
from server.app_sudoku.domain.sudoku_solver_model import SudokuBase


class SudokuGenerator(SudokuBase):
    _STARTING_SQUARES_EASY = 32
    _STARTING_SQUARES_HARD = 30

    def _unique_solution(self, sudoku: List[int]) -> bool:
        parsed_sudoku = self.parse_board(sudoku)

        if not parsed_sudoku:
            return False

        uniquely_solved_sudoku = self.search(parsed_sudoku, True)

        if not uniquely_solved_sudoku:
            return False

        return self.verify_solution(self.sudoku_to_list(uniquely_solved_sudoku))

    def _generate_sudoku(self, startin_squares: int) -> List[int]:
        sudoku = [0 for i in range(NUM_OF_SQUARES)]
        counter = 0

        while counter < startin_squares:
            index = random.randint(0, 80)

            if sudoku[index] == 0:
                value = random.randint(1, 9)
                sudoku[index] = value
                parsed_sudoku = self.parse_board(sudoku)

                if (
                    parsed_sudoku
                    and min(len(parsed_sudoku[square]) for square in SQUARES) > 0
                ):
                    counter += 1
                else:
                    sudoku[index] = 0

        return (
            sudoku
            if self._unique_solution(sudoku)
            else self._generate_sudoku(startin_squares)
        )

    @property
    def easy(self) -> List[int]:
        return self._generate_sudoku(self._STARTING_SQUARES_EASY)

    @property
    def hard(self) -> List[int]:
        return self._generate_sudoku(self._STARTING_SQUARES_HARD)
