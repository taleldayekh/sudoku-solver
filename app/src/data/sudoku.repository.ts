// import { SudokuModel } from '../models/models.interface';
import SudokuApi from './api/sudoku.api';

export default class Sudoku {
  public static async verifySolution(sudoku: number[]): Promise<boolean> {
    const res = await SudokuApi.verify(sudoku);
    return res.data.data;
  }
}
