import React, { useEffect } from 'react';
import { useWindowDimensions } from 'react-native';
import {
  SheetViewControllerProps,
  HideSheetGestureCtx,
} from '@/views/sheet/sheet.interface';
import { PanGestureHandler } from 'react-native-gesture-handler';
import Animated, {
  useSharedValue,
  useAnimatedGestureHandler,
  useAnimatedStyle,
  withSpring,
} from 'react-native-reanimated';
import styles from '@/views/sheet/sheet.styles';

const SheetViewController: React.FC<SheetViewControllerProps> = (
  props: SheetViewControllerProps,
) => {
  const { visible, children } = props;

  const closedSheetDimensions = useWindowDimensions().height;
  const openedSheetDimensions = useWindowDimensions().height / 2;
  const sheetVisibility = useSharedValue(closedSheetDimensions);

  const onHideSheetGesture = useAnimatedGestureHandler({
    onStart(_, context: HideSheetGestureCtx) {
      context.sheetVisibilityGestureStart = sheetVisibility.value;
    },
    onActive(event, context: HideSheetGestureCtx) {
      sheetVisibility.value =
        context.sheetVisibilityGestureStart + event.translationY;
    },
    onEnd() {
      const dismissSheetThreshold =
        sheetVisibility.value > openedSheetDimensions + 200;
      dismissSheetThreshold
        ? (sheetVisibility.value = closedSheetDimensions)
        : (sheetVisibility.value = openedSheetDimensions);
    },
  });

  const animatedStyles = useAnimatedStyle(() => {
    return {
      top: withSpring(sheetVisibility.value),
    };
  });

  useEffect(() => {
    visible !== undefined && (sheetVisibility.value = openedSheetDimensions);
  });

  return (
    <>
      <PanGestureHandler onGestureEvent={onHideSheetGesture}>
        <Animated.View style={[styles.sheet, animatedStyles]}>
          {children}
        </Animated.View>
      </PanGestureHandler>
    </>
  );
};

export default SheetViewController;
