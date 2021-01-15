from typing import Dict, List, Tuple

from server.app_sudoku.domain.sudoku_components import (
    NUM_OF_SQUARES,
    PEERS,
    SQUARES,
    SUDOKU_ROWS,
    UNITS,
)


class SudokuBase:
    _DIGITS = "123456789"

    @staticmethod
    def validate_sudoku_input(board: List[int]) -> bool:
        if len(board) != NUM_OF_SQUARES:
            return False

        for num in board:
            if not isinstance(num, int):
                return False

        if max(board) > SUDOKU_ROWS or min(board) < 0:
            return False

        if max(board) == 0:
            return False

        return True

    def _eliminate_digit(
        self, grid: Dict[int, str], index: int, digit: str
    ) -> Dict[int, str]:
        """
        Eliminate digit from digits in grid at index.
        If only one digit remains remove that digit
        from peers. If there is only one place in a unit
        for a digit, put it there. If elimination of a
        digit results in an empty square we have
        a contradiction and an unsolvable sudoku.
        """
        # Already removed
        if digit not in grid[index]:
            return grid

        grid[index] = grid[index].replace(digit, "")

        # Contradiction
        if len(grid[index]) == 0:
            return dict()

        if len(grid[index]) == 1:
            unique_digit = grid[index]

            if not all(
                self._eliminate_digit(grid, peer, unique_digit) for peer in PEERS[index]
            ):
                return dict()
        else:
            for unit in UNITS[index]:
                digit_places = []

                for unit_index in unit:
                    if digit in grid[unit_index]:
                        digit_places.append(unit_index)

                if len(digit_places) == 0:
                    return dict()

                if len(digit_places) == 1:
                    successful = self._assign_digit(grid, digit_places[0], digit)

                    if not successful:
                        return dict()

        return grid

    def _assign_digit(
        self, grid: Dict[int, str], index: int, digit: str
    ) -> Dict[int, str]:
        """
        Assign digit to a square by eliminating
        all digits at index except digit.
        """
        other_digits = grid[index].replace(digit, "")

        if all(
            self._eliminate_digit(grid, index, eliminated_digit)
            for eliminated_digit in other_digits
        ):
            return grid

        return dict()

    def parse_board(self, board: List[int]) -> Dict[int, str]:
        if not self.validate_sudoku_input(board):
            return dict()

        grid = dict()
        for index in range(NUM_OF_SQUARES):
            grid[index] = self._DIGITS

        for index, digit in enumerate(board):
            if digit != 0:
                self._assign_digit(grid, index, str(digit))

        return grid

    # TODO: Consider whether it makes sense making this method a part of the search method
    @staticmethod
    def _first_non_empty(sequence: List[Dict[int, str]]) -> Dict[int, str]:
        """
        Return first non-empty element
        """
        for element in sequence:
            if element:
                return element

        return dict()

    # TODO: Consider whether it makes sense making this method a part of the search method
    @staticmethod
    def _non_empty(sequence: List[Dict[int, str]]) -> Tuple[Dict[int, str], int]:
        # TODO: Should this have the same docstring as the first_non_empty method?
        """
        Return first non-empty element
        """
        true_element = dict()
        num = 0

        for element in sequence:
            if element:
                num += 1
                true_element = element

        return true_element, num

    def search(self, grid: Dict[int, str], only_unique: bool = False) -> Dict[int, str]:
        """
        Depth-first search and constraint propagation,
        try all possible values.
        """
        # Failed upstream
        if not grid:
            return dict()

        # Inconsistency
        if min(len(grid[s]) for s in SQUARES) == 0:
            return dict()

        # Solved
        if all(len(grid[s]) == 1 for s in SQUARES):
            return grid

        # Choose the unfilled squares with the fewest possibilities
        _, square = min(
            (len(grid[square]), square) for square in SQUARES if len(grid[square]) > 1
        )

        if only_unique:
            grid, num_solutions = self._non_empty(
                [
                    self.search(self._assign_digit(grid.copy(), square, digit))
                    for digit in grid[square]
                ]
            )
            if num_solutions > 1:
                return dict()
        else:
            grid = self._first_non_empty(
                [
                    self.search(self._assign_digit(grid.copy(), square, digit))
                    for digit in grid[square]
                ]
            )

        return grid

    @staticmethod
    def sudoku_to_list(grid: Dict[int, str]) -> List[int]:
        return [int(grid[index]) for index in grid]

    def verify_solution(self, board: List[int]) -> bool:
        digit_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

        if not board:
            return False

        if not self.validate_sudoku_input(board):
            return False

        for square in SQUARES:
            for unit in UNITS[square]:
                if set(board[index] for index in unit) != digit_set:
                    return False

        return True
