import axios from 'axios';
import React, { useState } from 'react';
import {SafeAreaView, View, Text, StatusBar, Button, TextInput} from 'react-native';

const App = () => {
  const [sudokuBoard, setSudokuBoard] = useState<any>([])
  const [loading, setLoading] = useState<boolean>(false)

  const generateSudoku = async () => {
      setSudokuBoard([])
      setLoading(true)
      const generatedSudoku = await axios.get('http://localhost:5000/api/v1/sudoku/generate')
      
      let sudokuRows = []
      console.log(generatedSudoku.data.data)

      while (generatedSudoku.data.data.length > 0) {
        sudokuRows.push(generatedSudoku.data.data.splice(0, 9))
      }
      console.log(sudokuRows)
      setLoading(false)
      setSudokuBoard(sudokuRows)
      
  }

  return (
    <>
    {sudokuBoard.length ? (
      <>
      <StatusBar barStyle="dark-content" />
      <SafeAreaView>
        {
          sudokuBoard.map((sudokuBox: number[], index: number) => 
            <View key={index} style={{flexDirection: 'row', height: 45, marginLeft: 5, marginRight: 5}}>
              {
                sudokuBox.map((sudokuSquare: number, index: number) => 
                  sudokuSquare > 0 ? <View key={index} style={{ 
                    flex: 1,
                    borderColor: 'gray',
                    borderWidth: 1,
                    justifyContent: 'center',
                    alignItems: 'center'
                  }}>
                  <Text style={{fontSize: 25, color: 'red'}}>
                    {sudokuSquare.toString()}
                  </Text>
                  </View> : <View key={index} style={{ flex: 1, borderColor: 'gray', borderWidth: 1, justifyContent: 'center', alignItems: 'center'}}>
                    <TextInput style={{fontSize: 25}}>
                    </TextInput>
                  </View>
                )
              }
            </View>
          )
        }
        <Button title="Generate Sudoku" onPress={() => generateSudoku()}/>
      </SafeAreaView>
      </>
    ) : (
      <SafeAreaView>
        <View style={{height: 405, width: 405, marginLeft: 5, marginRight: 5, borderColor: 'gray', borderWidth: 1, justifyContent: 'center', alignItems: 'center'}}>
          {loading ? <Text style={{fontSize: 30}}>Loading...</Text> : <></>}
        </View>
        <Button title="Generate Sudoku" onPress={() => generateSudoku()}/>
      </SafeAreaView>
    )}
    </>
  );
};

export default App;
