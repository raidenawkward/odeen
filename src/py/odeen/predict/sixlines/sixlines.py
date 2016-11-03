# coding = utf-8

import sys

from predict.predict import *
from predict.sixlines.diceengine import DiceEngine
from core.edengine import *
from core.ed import *
from core.ed2 import *



class SixLines(Predict):
    '''
    predict by 'six lines' method
    '''

    SYMBOL_UNKNOWN = -1
    DEF_NAME = 'Six Lines'
    DEF_DICE_TIMES = 6

    KEY_EDENGINE_VERSION = 'edengineversion'
    KEY_ED_DOWN = 'eddown'
    KEY_ED_UP = 'edup'

    KEY_SYMBOL_LIST = 'symbollist'

    KEY_LIST = [
        KEY_EDENGINE_VERSION,
        KEY_ED_DOWN,
        KEY_ED_UP,
        KEY_SYMBOL_LIST
    ]

    def __init__(self, edengine):
        super().__init__()
        self._edengine = edengine
        self._diceengine = DiceEngine()

        self._step = 0
        self._initSymbolList()
        self.getDict()[Predict.KEY_NAME] = SixLines.DEF_NAME

    def getDictKeyList(self):
        l = super().getDictKeyList()
        l.extend(SixLines.KEY_LIST)
        return l

    def _initSymbolList(self):
        l = self.getDict()[SixLines.KEY_SYMBOL_LIST]
        if l is None:
            l = []

        for i in range(0, 6):
            l.append(SixLines.SYMBOL_UNKNOWN)

        self.getDict()[SixLines.KEY_SYMBOL_LIST] = l

    def getEdEngine(self):
        return self._edengine

    def getDiceEngine(self):
        return self._diceengine

    def getSymbolList(self):
        return self.getDict()[SixLines.KEY_SYMBOL_LIST]

    def reset(self):
        super().reset()
        self._initSymbolList()

    def getStep(self):
        return self._step

    def isFinished(self):
        return self.getStep() >= SixLines.DEF_DICE_TIMES

    def dice(self):
        if self.isFinished():
            return False

        step = self.getStep()
        diceEngine = self.getDiceEngine()
        self.getSymbolList()[step] = diceEngine.dice()

        self._step = self._step + 1

        return True

    def _checkSymbols(self):
        pass

    def _generateResult(self):
        pass

    def getResult(self):
        pass