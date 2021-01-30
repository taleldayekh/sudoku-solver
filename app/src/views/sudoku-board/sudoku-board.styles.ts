import { Dimensions, StyleSheet } from 'react-native';
import { SUDOKU_ROW_COL_COUNT } from './constants';

const SIDE_MARGINS = 10;
const BORDER_WIDTH = 1;
const BOX_BORDER_WIDTH = 3;

const deviceViewportWidth = Dimensions.get('window').width;
const cellWidth =
  (deviceViewportWidth - 2 * SIDE_MARGINS) / SUDOKU_ROW_COL_COUNT;

export default StyleSheet.create({
  board: {
    borderRadius: 8,
    borderWidth: BORDER_WIDTH,
    marginHorizontal: SIDE_MARGINS,

    // ! Remove
    marginTop: 200,
  },
  row: {
    borderBottomWidth: BORDER_WIDTH,
    flexDirection: 'row',
    height: cellWidth,
  },
  rowNoBorder: {
    borderBottomWidth: undefined,
  },
  cell: {
    alignItems: 'center',
    borderRightWidth: BORDER_WIDTH,
    flex: 1,
    justifyContent: 'center',
  },
  cellNoBorder: {
    borderRightWidth: undefined,
  },
  boxRowBorder: {
    borderBottomWidth: BOX_BORDER_WIDTH,
  },
  boxColBorder: {
    borderRightWidth: BOX_BORDER_WIDTH,
  },
});
