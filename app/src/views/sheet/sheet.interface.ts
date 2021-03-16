import { ReactNode } from 'react';

export interface SheetViewControllerProps {
  visible: boolean | undefined;
  children: ReactNode;
}

export type HideSheetGestureCtx = {
  sheetVisibilityGestureStart: number;
};
