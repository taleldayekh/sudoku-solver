import React, { useEffect, useState } from 'react';
import { Button, Text, View } from 'react-native';
import Sudoku from '../../data/sudoku.repository';
import { SudokuBoard } from '../../view-models/view-models.interface';
import SudokuBoardView from './SudokuBoardView';
import { DefaultCandidatesIndexes } from './sudoku-board.interface';

const SudokuBoardViewController = () => {
  const [sudokuBoard, setSudokuBoard] = useState<SudokuBoard>([]);
  const [isValidSolution, setIsValidSolution] = useState<boolean | undefined>(
    undefined,
  );
  const [
    defaultCandidatesIndexes,
    // setDefaultCandidatesIndexes,
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

        if (!candidatesIndexes.length) {
          return defaultCandidatesIndexes;
        }

        defaultCandidatesIndexes[index] = candidatesIndexes;
        return defaultCandidatesIndexes;
      },
      {},
    );
  };

  console.log(getDefaultCandidatesIndexes);

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

  // useEffect(() => {
  //   // TODO: Extend empty object check and remove duplication
  //   if (
  //     sudokuBoard.length &&
  //     Object.keys(defaultCandidatesIndexes).length !== 0
  //   ) {
  //     return;
  //   }

  //   setSudokuBoard(dummySudoku);
  //   setDefaultCandidatesIndexes(getDefaultCandidatesIndexes());
  // }, [sudokuBoard, defaultCandidatesIndexes, getDefaultCandidatesIndexes]);

  useEffect(() => {
    if (sudokuBoard.length === 0 || sudokuBoard.flat().includes(0)) {
      return;
    }
    Sudoku.verifySolution(sudokuBoard.flat())
      .then((res) => {
        console.log(res);
        setIsValidSolution(res);
      })
      .catch((err) => console.log(err));
  }, [sudokuBoard]);

  return (
    <>
      {sudokuBoard &&
      Object.keys(defaultCandidatesIndexes).length !== 0 &&
      isValidSolution === undefined ? (
        <SudokuBoardView
          sudokuBoard={sudokuBoard}
          defaultCandidatesIndexes={defaultCandidatesIndexes}
          editCandidate={editCandidate}
        />
      ) : (
        <>
          {isValidSolution === true ? (
            <View
              style={{
                paddingTop: 400,
                alignItems: 'center',
              }}>
              <Text
                style={{
                  fontSize: 60,
                }}>
                👍
              </Text>
              <Button
                title="Back"
                onPress={() => {
                  setSudokuBoard(dummySudoku);
                  setIsValidSolution(undefined);
                }}
              />
            </View>
          ) : (
            <View
              style={{
                paddingTop: 400,
                alignItems: 'center',
              }}>
              <Text
                style={{
                  fontSize: 60,
                }}>
                👎
              </Text>
              <Button
                title="Back"
                onPress={() => {
                  setIsValidSolution(undefined);
                }}
              />
            </View>
          )}
        </>
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

// ! Solution
// const solved = [
//   [2, 1, 4, 3], // 1
//   [3, 6, 1], // 2
//   [5, 6, 9, 1, 8, 4], // 3
//   [2, 8, 6, 3, 9], // 4
//   [1, 7, 4, 3, 2], // 5
//   [3, 4, 5, 1, 8, 6, 9, 7], // 6
//   [8, 9, 4, 7, 2, 1, 5, 6], // 7
//   [7, 3, 1, 4, 9], // 8
//   [1, 5, 9, 4, 2], // 9
// ];
