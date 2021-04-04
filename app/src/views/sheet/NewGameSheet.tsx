import React from 'react';
import { View, Button } from 'react-native';
import styles from '@/views/sheet/sheet.styles';

const NewGameSheet: React.FC = () => {
  return (
    <View style={styles.newGame}>
      <Button testID="easy-game-button" title="Easy" onPress={() => {}} />
      <Button testID="medium-game-button" title="Medium" onPress={() => {}} />
      <Button testID="hard-game-button" title="Hard" onPress={() => {}} />
    </View>
  );
};

export default NewGameSheet;
