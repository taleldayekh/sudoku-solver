import React from 'react';
import { fireEvent, render } from '@testing-library/react-native';
import { withReanimatedTimer, advanceAnimationByTime } from 'react-native-reanimated/src/reanimated2/jestUtils';
import HomeViewController from '@/views/home/HomeViewController';

describe('HomeViewController', () => {
  test('clicking new game button displays new game sheet', () => {
    withReanimatedTimer(() => {
      const { getByTestId } = render(<HomeViewController/>)

      const newGameButton = getByTestId('new-game-button')
      const newGameSheet = getByTestId('new-game-sheet')

      expect(newGameSheet.props.animatedStyle.value.top).toBe(1334)
      
      fireEvent.press(newGameButton)
      advanceAnimationByTime(500)
      
      expect(newGameSheet.props.animatedStyle.value.top).toBeLessThan(1334)
    })
  })
})
