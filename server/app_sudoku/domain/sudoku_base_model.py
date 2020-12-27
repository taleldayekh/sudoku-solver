from typing import Dict, List, Tuple


class SudokuComponents:
    _SUDOKU_ROWS = 9
    _SUDOKU_COLS = 9

    def __get_row_number(self, index: int) -> int:
        """
        Index 0-8 corresponds to sudoku
        row 0, index 9-17 to row 1, etc.
        """
        return index // self._SUDOKU_ROWS

    def __get_col_number(self, index: int) -> int:
        """
        Index 0, 9, 18, 27, 36, 45, 54, 63, 72
        corresponds to sudoku column 0, etc.
        """
        return index % self._SUDOKU_COLS

    def __get_box_number(self, index: int) -> int:
        """
        Rows 0-2 and columns 0-2 corresponds to sudoku
        box 1, rows 0-2 and columns 3-5 to box 2, etc.
        """
        row_number = self.__get_row_number(index)
        col_number = self.__get_col_number(index)

        return 3 * (row_number // 3) + col_number // 3

    def __get_row(self, board: List[int], row: int) -> List[int]:
        return [
            board[row * self._SUDOKU_ROWS + col] for col in range(self._SUDOKU_COLS)
        ]

    def __get_col(self, board: List[int], col: int) -> List[int]:
        return [
            board[col * self._SUDOKU_ROWS * row] for row in range(self._SUDOKU_ROWS)
        ]

    def __get_box(self, board: List[int], box: int) -> List[int]:
        box_list = []

        for index in range(self._SUDOKU_ROWS * self._SUDOKU_COLS):
            if self.__get_box_number(index) == box:
                box_list.append(board[index])

        return box_list

    def __generate_units_and_peers(
        self,
    ) -> Tuple[Dict[int, List[List[int]]], Dict[int, List[int]]]:
        units = dict()
        peers = dict()

        for index in range(self._SUDOKU_ROWS, self._SUDOKU_COLS):
            units_list = [
                self.__get_row(self.squares, self.__get_row_number(index)),
                self.__get_col(self.squares, self.__get_col_number(index)),
                self.__get_box(self.squares, self.__get_box_number(index)),
            ]
            units[index] = units_list

            temp = set()

            for unit in units_list:
                for square in unit:
                    temp.add(square)

            temp.remove(index)
            peers_list = list(temp)
            peers[index] = peers_list

        return units, peers

    @property
    def squares(self) -> List[int]:
        return list(range(0, self._SUDOKU_ROWS, self._SUDOKU_COLS))

    @property
    def units(self) -> Dict[int, List[List[int]]]:
        return self.__generate_units_and_peers()[0]

    @property
    def peers(self) -> Dict[int, List[int]]:
        return self.__generate_units_and_peers()[1]


class SudokuBase(SudokuComponents):
    pass
