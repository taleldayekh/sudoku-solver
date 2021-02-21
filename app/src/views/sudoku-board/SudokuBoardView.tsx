import React from 'react';
import { View } from 'react-native';
import { SUDOKU_ROW_COL_COUNT } from './constants';
import { SudokuBoardViewProps } from './sudoku-board.interface';
import SudokuCellView from '../sudoku-cell/SudokuCellView';
import styles from './sudoku-board.styles';

const BOX_BORDER_INDEX = [2, 5];
const LAST_ROW_COL = SUDOKU_ROW_COL_COUNT - 1;

const SudokuBoardView: React.FC<SudokuBoardViewProps> = (props) => {
  // TODO: Perhaps consider adding as context?
  const { sudokuBoard, defaultCandidatesIndexes, editCandidate } = props;

  return (
    <View style={styles.board}>
      {sudokuBoard.map((sudokuRow: number[], rowIndex: number) => (
        <View
          style={[
            styles.row,
            rowIndex === LAST_ROW_COL && styles.rowNoBorder,
            BOX_BORDER_INDEX.includes(rowIndex) && styles.boxRowBorder,
          ]}
          key={rowIndex}>
          {sudokuRow.map((sudokuCell: number, cellIndex: number) => (
            <View
              style={[
                styles.cell,
                cellIndex === LAST_ROW_COL && styles.cellNoBorder,
                BOX_BORDER_INDEX.includes(cellIndex) && styles.boxColBorder,
              ]}
              key={cellIndex}>
              <SudokuCellView
                defaultCandidatesIndexes={defaultCandidatesIndexes}
                cellIndex={cellIndex}
                rowIndex={rowIndex}
                editCandidate={editCandidate}>
                {sudokuCell}
              </SudokuCellView>
            </View>
          ))}
        </View>
      ))}
    </View>
  );
};

export default SudokuBoardView;
