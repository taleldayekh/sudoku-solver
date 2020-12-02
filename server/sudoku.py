import json
from typing import List

NROWS = 9
NCOLS = 9


def writeSudokuToFile(board: List[int], filename: str) -> None:
    with open(filename, "w") as outfile:
        json.dump(board, outfile)


def readSudokuFromFile(filename: str) -> List[int]:
    with open(filename, "r") as infile:
        return json.load(infile)


def printSudoku_simple(board: List[int]) -> None:
    for row in range(NROWS):
        for col in range(NCOLS):
            num = board[row * NROWS + col]
            print(num, end=" ")
        print(f"\n", end="")


def printSudoku(board: List[int]) -> None:
    divider = "|———————|———————|———————|"
    for row in range(NROWS):
        if row % 3 == 0:
            print(divider)
        for col in range(NCOLS):
            if col % 3 == 0:
                print("| ", end="")
            num = board[row * NROWS + col]
            if num > 0:
                print(num, end=" ")
            else:
                print(" ", end=" ")
        print("|")
    print(divider)



S = readSudokuFromFile("example_sudoku.json")
printSudoku(S)

S_solved = readSudokuFromFile("example_sudoku_solved.json")
printSudoku(S_solved)
