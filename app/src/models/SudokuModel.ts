import { SudokuModel as SudokuModelInterface } from 'src/models/models.interface';

export class SudokuModel implements SudokuModelInterface {
  constructor(public sudoku: number[]) {}
}
