import React, { useState, useEffect } from 'react';
import { SudokuBoard } from '../../view-models/view-models.interface';
import { DefaultCandidatesIndexes } from './sudoku-board.interface';
import SudokuBoardView from './SudokuBoardView';

const SudokuBoardViewController = () => {
  const [sudokuBoard, setSudokuBoard] = useState<SudokuBoard>([]);
  const [
    defaultCandidatesIndexes,
    setDefaultCandidatesIndexes,
  ] = useState<DefaultCandidatesIndexes>({});

  const getDefaultCandidatesIndexes = (): DefaultCandidatesIndexes => {
    return sudokuBoard.reduce(
      (
        defaultCandidatesIndexes: DefaultCandidatesIndexes,
        sudokuRow: number[],
        index: number,
      ) => {
        const candidatesIndexes = sudokuRow.flatMap(
          (sudokuCell: number, index: number) =>
            sudokuCell !== 0 ? [index] : [],
        );

        if (!candidatesIndexes.length) return defaultCandidatesIndexes;

        defaultCandidatesIndexes[index] = candidatesIndexes;
        return defaultCandidatesIndexes;
      },
      {},
    );
  };

  const editCandidate = (
    rowIndex: number,
    cellIndex: number,
    candidate: number,
  ): void => {
    const updatedSudokuBoard = sudokuBoard.reduce(
      (sudokuBoard: SudokuBoard, sudokuRow: number[], index: number) => {
        if (index === rowIndex) {
          sudokuRow[cellIndex] = candidate;
        }
        sudokuBoard.push(sudokuRow);

        return sudokuBoard;
      },
      [],
    );

    setSudokuBoard(updatedSudokuBoard);
  };

  useEffect(() => {
    // TODO: Extend empty object check and remove duplication
    if (
      sudokuBoard.length &&
      Object.keys(defaultCandidatesIndexes).length !== 0
    )
      return;

    setSudokuBoard(dummySudoku);
    setDefaultCandidatesIndexes(getDefaultCandidatesIndexes());
  });

  return (
    <>
      {sudokuBoard && Object.keys(defaultCandidatesIndexes).length !== 0 ? (
        <SudokuBoardView
          sudokuBoard={sudokuBoard}
          defaultCandidatesIndexes={defaultCandidatesIndexes}
          editCandidate={editCandidate}
        />
      ) : (
        <></>
      )}
    </>
  );
};

export default SudokuBoardViewController;

// //! Delete
const dummySudoku = [
  [7, 0, 0, 8, 0, 5, 9, 6, 0],
  [4, 0, 8, 0, 7, 9, 2, 5, 0],
  [0, 0, 0, 0, 3, 2, 0, 7, 0],
  [0, 0, 0, 0, 0, 7, 4, 1, 5],
  [9, 0, 0, 0, 5, 6, 0, 0, 8],
  [0, 0, 0, 2, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 3, 0],
  [6, 0, 2, 5, 8, 0, 0, 0, 0],
  [0, 0, 3, 0, 6, 0, 7, 8, 0],
];
