import { SudokuBoard } from '../../view-models/view-models.interface';

export type EditCandidate = (
  rowIndex: number,
  cellIndex: number,
  candidate: number,
) => void;

export interface DefaultCandidatesIndexes {
  [key: number]: number[];
}

export interface SudokuBoardViewProps {
  sudokuBoard: SudokuBoard;
  defaultCandidatesIndexes: DefaultCandidatesIndexes;
  editCandidate: EditCandidate;
}
