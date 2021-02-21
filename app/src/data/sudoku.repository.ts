import SudokuApi from './api/sudoku.api';
import { SudokuModel } from '../models/models.interface';

export default class Sudoku {
  public static async verifySolution(sudoku: number[]): Promise<boolean> {
    const res = await SudokuApi.verify(sudoku);
    return res.data.data;
  }
}
