const sudoku_example = [5, 3, 0, 0, 7, 0, 0, 0, 0, 6, 0, 0, 1, 9, 5, 0, 0, 0, 0, 9, 8, 0, 0, 0, 0, 6, 0, 8, 0, 0, 0, 6, 0, 0, 0, 3, 4, 0, 0, 8, 0, 3, 0, 0, 1, 7, 0, 0, 0, 2, 0, 0, 0, 6, 0, 6, 0, 0, 0, 0, 2, 8, 0, 0, 0, 0, 4, 1, 9, 0, 0, 5, 0, 0, 0, 0, 8, 0, 0, 7, 9];

const SUDOKU_ROWS = 9;
const SUDOKU_COLS = 9;
const NUM_OF_SQUARES = SUDOKU_ROWS * SUDOKU_COLS;
//SQUARES = list(range(NUM_OF_SQUARES))


function printSudoku(sudoku: number[]): void {
   for(let row=0; row<SUDOKU_ROWS ;row++){
      let s = '';
      let delimiter = '------+-------+------';
      for(let col=0; col<SUDOKU_COLS ;col++){
         if (sudoku_example[row*SUDOKU_ROWS+col] == 0) {
            s +='  '
         } else {
            s += sudoku_example[row*SUDOKU_ROWS+col].toString()+' ';
         }                  
         if((col+1)%3 === 0 && (col+1)<SUDOKU_COLS){
            s+='| ';
         }
      }
      console.log(s);
      if((row+1)%3 === 0 && (row+1)<SUDOKU_ROWS){
            console.log(delimiter);
         }  
   }
}

function get_row_number(index: number): number {
   return Math.floor(index/SUDOKU_ROWS);
}

function get_col_number(index: number): number {
   return index % SUDOKU_COLS;
}

function get_box_number(index: number): number {   
   let row_number = get_row_number(index);
   let col_number = get_col_number(index);   
   return (3*Math.floor(row_number/3) + Math.floor(col_number/3));   
}

function get_row(board: number[], row_number: number): number[] {
   let row:number[] = new Array(SUDOKU_COLS);
   for(let col=0; col<SUDOKU_COLS; col++){
      row[col] = board[row_number*SUDOKU_ROWS + col];
   }
   return row;
}

function get_col(board: number[], col_number: number): number[] {
   let col:number[] = new Array(SUDOKU_ROWS);
   for(let row=0; row<SUDOKU_ROWS; row++){
      col[row] = board[col_number + row*SUDOKU_COLS];
   }
   return col;
}

function get_box(board: number[], box_number: number): number[] {
   let box:number[] = new Array(SUDOKU_ROWS);
   let counter = 0;
   for(let index=0; index<NUM_OF_SQUARES; index++){
      if (get_box_number(index) === box_number) {
         box[counter] = board[index];
         counter += 1;
      }
   }
   return box;
}

function generate_squares(num_squares: number): number[] {
   let squares:number[] = new Array(num_squares);
   for(let index=0; index<num_squares; index++) {
      squares[index] = index;
   }
   return squares;
}


const generate_units = (num_squares: number, squares: number[]): any => {
   let units = new Array(num_squares);
   for(let index=0; index<num_squares; index++) {
      units[index] = [get_row(squares, get_row_number(index)), 
                      get_col(squares, get_col_number(index)), 
                      get_box(squares, get_box_number(index))];
   }
   return units;
}


printSudoku(sudoku_example);


const SQUARES = generate_squares(NUM_OF_SQUARES);
const UNITS = generate_units(NUM_OF_SQUARES, SQUARES);

console.log(UNITS);