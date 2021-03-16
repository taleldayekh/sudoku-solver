import React from 'react';
import { HomeViewProps } from '@/views/home/home.interface';
import { View, Button } from 'react-native';
import styles from '@/views/home/home.styles';

const HomeView: React.FC<HomeViewProps> = (props: HomeViewProps) => {
  const { newGameAction } = props;

  return (
    <View style={styles.wrapper}>
      <Button title="New Game" onPress={() => newGameAction()} />
    </View>
  );
};

export default HomeView;
