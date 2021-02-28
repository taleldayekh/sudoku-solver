import React from 'react';
import { Text, TextInput } from 'react-native';
import { SudokuCellProps } from './sudoku-cell.interface';
import styles from './sudoku-cell.styles';

const SudokuCellView: React.FC<SudokuCellProps> = (props) => {
  const {
    defaultCandidatesIndexes,
    children,
    rowIndex,
    cellIndex,
    editCandidate,
  } = props;

  return (
    <>
      {defaultCandidatesIndexes[rowIndex].includes(cellIndex) ? (
        <Text style={styles.cellContent}>{children}</Text>
      ) : (
        <TextInput
          style={styles.cellContent}
          // TODO: Add validation
          onChangeText={(candidate) =>
            editCandidate(rowIndex, cellIndex, Number(candidate))
          }
        />
      )}
    </>
  );
};

export default SudokuCellView;
