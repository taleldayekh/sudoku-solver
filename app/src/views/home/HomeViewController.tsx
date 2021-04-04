import React, { useState } from 'react';
import HomeView from '@/views/home/HomeView';
import SheetViewController from '@/views/sheet/SheetViewController';
import NewGameSheet from '@/views/sheet/NewGameSheet';

const HomeViewController: React.FC = () => {
  const [newGameSheetIsVisible, setNewGameSheetIsVisible] = useState<
    boolean | undefined
  >(undefined);

  const displayNewGameSheet = (): void => {
    setNewGameSheetIsVisible(!newGameSheetIsVisible);
  };

  return (
    <>
      <HomeView newGameAction={displayNewGameSheet} />
      <SheetViewController visible={newGameSheetIsVisible}>
        <NewGameSheet />
      </SheetViewController>
    </>
  );
};

export default HomeViewController;
