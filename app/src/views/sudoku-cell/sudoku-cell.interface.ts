import {
  DefaultCandidatesIndexes,
  EditCandidate,
} from '../sudoku-board/sudoku-board.interface';

export interface SudokuCellProps {
  children: number;
  defaultCandidatesIndexes: DefaultCandidatesIndexes;
  rowIndex: number;
  cellIndex: number;
  editCandidate: EditCandidate;
}
