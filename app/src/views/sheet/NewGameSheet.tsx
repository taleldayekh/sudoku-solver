import React from 'react';
import { View, Button } from 'react-native';
import styles from '@/views/sheet/sheet.styles';

const NewGameSheet: React.FC = () => {
  return (
    <View style={styles.newGame}>
      <Button title="Easy" onPress={() => {}} />
      <Button title="Medium" onPress={() => {}} />
      <Button title="Hard" onPress={() => {}} />
    </View>
  );
};

export default NewGameSheet;
