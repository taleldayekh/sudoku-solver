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

# 0-8 is row 0 , 9-17 row 1 etc.
def getRowNumber(index: int) -> int:
    return index//NROWS

# [0,9,18,27,36,45,54,63,72] is column 0 etc.
def getColumnNumber(index: int) -> int:
    return index%NCOLS

# rows 0-2 and column 0-2 is box 1, rows 0-2 and column 3-5 is box 2 etc.
def getBoxNumber(index: int) -> int:
    return 3*(getRowNumber(index)//3) + getColumnNumber(index)//3

index_board = [i for i in range(81)]
printSudoku(index_board)

for i in index_board:
    r = getRowNumber(i)
    c = getColumnNumber(i)
    b = getBoxNumber(i)
    print(f"{i}: {r}; {c}; {b}")
