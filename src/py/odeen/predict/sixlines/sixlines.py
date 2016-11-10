# coding = utf-8

import sys
import time

from predict.predict import *
from predict.sixlines.diceengine import DiceEngine
from core.edengine import *
from core.ed import *
from core.ed2 import *



class SixLines(Predict):
    '''
    predict by 'six lines' method
    '''

    TYPE = 'SIXLINES'
    SYMBOL_UNKNOWN = -1
    DEF_NAME = 'Six Lines'
    DEF_DICE_TIMES = 6

    KEY_EDENGINE_VERSION = 'edengineversion'
    KEY_ED_DOWN = 'eddown'
    KEY_ED_UP = 'edup'

    KEY_SYMBOL_LIST = 'symbollist'
    KEY_PREDICT_TIME = 'predicttime'

    KEY_LIST = [
        KEY_EDENGINE_VERSION,
        KEY_ED_DOWN,
        KEY_ED_UP,
        KEY_SYMBOL_LIST,
        KEY_PREDICT_TIME
    ]

    def __init__(self, edengine):
        super().__init__()
        self._edengine = edengine
        self._diceengine = DiceEngine()
        self._id = 0

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
        else:
            l.clear()

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
        self._step = 0
        self._initSymbolList()

    def getStep(self):
        return self._step

    def isFinished(self):
        return self.getStep() >= SixLines.DEF_DICE_TIMES

    def isStarted(self):
        res = False
        l = self.getSymbolList()
        if l is None:
            return res

        for d in l:
            if d != SixLines.SYMBOL_UNKNOWN:
                return True

        return res

    def dice(self):
        if self.isFinished():
            self._id = self._id + 1
            return (False, None, None)

        step = self.getStep()
        diceEngine = self.getDiceEngine()
        self.getSymbolList()[step], diceList = diceEngine.dice()

        self._step = self._step + 1

        self.getDict()[SixLines.KEY_PREDICT_TIME] = time.time()

        return (True, self.getSymbolList()[step], diceList)

    def _checkSymbols(self):
        diceList = self.getSymbolList()
        ed2 = self.getEdEngine().findEd2(symbolList=diceList)

        self.getDict()[Predict.KEY_ID] = str(self.getDict()[SixLines.KEY_PREDICT_TIME]) + '.' + str(self._id)
        eds = ed2.getEds()
        self.getDict()[Predict.KEY_TYPE] = SixLines.TYPE
        self.getDict()[SixLines.KEY_ED_UP] = eds[0]
        self.getDict()[SixLines.KEY_ED_DOWN] = eds[1]
        self.getDict()[SixLines.KEY_EDENGINE_VERSION] = self.getEdEngine().getVersion()
        self.getDict()[Predict.KEY_CONCLUSION] = ed2.getName()

        return ed2

    def getResult(self):
        result = self._checkSymbols()
        return result
