import axios, { AxiosResponse } from 'axios';
import { API_BASE_URL } from './constants';
// import { SudokuModel } from '../../models/models.interface';
import { SudokuVerifyResponse } from './sudoku.api.interface';

const SUDOKU_URL = 'sudoku';

export default class SudokuApi {
  public static verify(
    sudoku: number[],
  ): Promise<AxiosResponse<SudokuVerifyResponse>> {
    return axios.post(`${API_BASE_URL}/${SUDOKU_URL}/verify`, {
      sudoku: sudoku,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }
}
