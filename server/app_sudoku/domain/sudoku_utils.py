import random
from typing import Dict, List, Tuple

NROWS = 9
NCOLS = 9
DIGITS = "123456789"
DIGIT_SET = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# 0-8 is row 0 , 9-17 row 1 etc.
def get_row_number(index: int) -> int:
    return index // NROWS


# 0,9,18,27,36,45,54,63,72 is column 0 etc.
def get_column_number(index: int) -> int:
    return index % NCOLS


# rows 0-2 and column 0-2 is box 1, rows 0-2 and column 3-5 is box 2 etc.
def get_box_number(index: int) -> int:
    return 3 * (get_row_number(index) // 3) + get_column_number(index) // 3


def get_row(board: List[int], row: int) -> List[int]:
    return [board[row * NROWS + col] for col in range(NCOLS)]


def get_column(board: List[int], column: int) -> List[int]:
    return [board[column + NROWS * row] for row in range(NROWS)]


def get_box(board: List[int], box: int) -> List[int]:
    boxlist = []
    for index in range(NROWS * NCOLS):
        if get_box_number(index) == box:
            boxlist.append(board[index])
    return boxlist


def generate_squares_units_peers() -> Tuple[
    List[int], Dict[int, List[List[int]]], Dict[int, List[int]]
]:
    squares = list(range(0, NROWS * NCOLS))
    units = dict()
    peers = dict()
    for index in range(NROWS * NCOLS):
        unitlist = [
            get_row(squares, get_row_number(index)),
            get_column(squares, get_column_number(index)),
            get_box(squares, get_box_number(index)),
        ]
        units[index] = unitlist

        temp = set()
        for unit in unitlist:
            for square in unit:
                temp.add(square)
        temp.remove(index)
        peers_list = list(temp)
        peers[index] = peers_list
    return squares, units, peers


SQUARES, UNITS, PEERS = generate_squares_units_peers()


def validate_sudoku_input(board: List[int]) -> bool:
    if len(board) != NROWS * NCOLS:
        return False
    for num in board:
        if isinstance(num, int):
            continue
        return False
    if max(board) > NROWS or min(board) < 0:
        return False
    if max(board) == 0:
        return False
    return True


def initialize_grid() -> Dict[int, str]:
    grid = dict()
    for index in range(NROWS * NCOLS):
        grid[index] = DIGITS
    return grid


def parse_board(board: List[int]) -> Dict[int, str]:
    if not validate_sudoku_input(board):
        return dict()
    grid = initialize_grid()
    for index, digit in enumerate(board):
        if digit != 0:
            assign(grid, index, str(digit))
    return grid


def assign(grid: Dict[int, str], index: int, digit: str) -> Dict[int, str]:
    """Assign digit to a square by eliminating all digits
    at index except digit"""
    other_digits = grid[index].replace(digit, "")
    if all(eliminate(grid, index, elim_digit) for elim_digit in other_digits):
        return grid
    return dict()


def eliminate(grid: Dict[int, str], index: int, digit: str) -> Dict[int, str]:
    """Eliminate digit from digits in grid at index.
    If only one digit remains remove that digit from peers.
    If there is only one place in a unit for a digit, put it there.
    If elimination of a digit results in an empty square we have
    a contradiction and an unsolvable sudoku."""
    # Already removed
    if digit not in grid[index]:
        return grid
    grid[index] = grid[index].replace(digit, "")

    # Contradiction
    if len(grid[index]) == 0:
        return dict()
    if len(grid[index]) == 1:
        unique_digit = grid[index]
        if not all(eliminate(grid, peer, unique_digit) for peer in PEERS[index]):
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
                successful = assign(grid, digit_places[0], digit)
                if not successful:
                    return dict()
    return grid


def search(grid: Dict[int, str], only_unique: bool = False) -> Dict[int, str]:
    """Depth-first search and constraint propagation,
    try all possible values."""
    if not grid:
        return dict()  # Failed upstream
    if min(len(grid[s]) for s in SQUARES) == 0:
        return dict()  # inconsistency
    if all(len(grid[s]) == 1 for s in SQUARES):
        return grid  # Solved!
    # Choose the unfilled square s with the fewest possibilities
    _, square = min(
        (len(grid[square]), square) for square in SQUARES if len(grid[square]) > 1
    )
    if only_unique:
        grid, num_solutions = non_empty(
            [search(assign(grid.copy(), square, digit)) for digit in grid[square]]
        )
        if num_solutions > 1:
            return dict()
    else:
        grid = first_non_empty(
            [search(assign(grid.copy(), square, digit)) for digit in grid[square]]
        )
    return grid


def first_non_empty(sequence: List[Dict[int, str]]) -> Dict[int, str]:
    # Return first non-empty element
    for element in sequence:
        if element:
            return element
    return dict()


def non_empty(sequence: List[Dict[int, str]]) -> Tuple[Dict[int, str], int]:
    # Return first non-empty element
    true_element = dict()
    num = 0
    for element in sequence:
        if element:
            num += 1
            true_element = element
    return true_element, num


def sudoku_to_list(grid: Dict[int, str]) -> List[int]:
    return [int(grid[index]) for index in grid]


def solve_sudoku(board: List[int]) -> List[int]:
    output = parse_board(board)
    if not output:
        return []
    output = search(output)
    if not output:
        return []
    output_list = sudoku_to_list(output)
    return output_list if verify_solution(output_list) else []


def has_unique_solution(board: List[int]) -> bool:
    output = parse_board(board)
    if not output:
        return False
    output = search(output, True)
    if not output:
        return False
    return verify_solution(sudoku_to_list(output))


def verify_solution(board: List[int]) -> bool:
    if not board:
        return False
    if not validate_sudoku_input(board):
        return False
    for square in SQUARES:
        for unit in UNITS[square]:
            if set(board[index] for index in unit) != DIGIT_SET:
                return False
    return True


def get_hint(board: List[int], solved: List[int]) -> List[int]:
    if not solved:
        return []
    new_squares = []
    for index, square in enumerate(board):
        if square == 0:
            new_squares.append([index, solved[index]])
    if not new_squares:
        return []
    return random.choice(new_squares)


def generate_sudoku(number_of_non_empty: int) -> List[int]:
    output = [0 for i in range(NROWS * NCOLS)]
    counter = 0
    while counter < number_of_non_empty:
        index = random.randint(0, 80)
        if output[index] == 0:
            value = random.randint(1, 9)
            output[index] = value
            grid = parse_board(output)
            if grid and min(len(grid[s]) for s in SQUARES) > 0:
                counter += 1
            else:
                output[index] = 0
    return (
        output if has_unique_solution(output) else generate_sudoku(number_of_non_empty)
    )
