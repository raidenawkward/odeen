# coding = utf-8

import sys

from predict.predict import *
from core.edengine import *
from core.ed import *
from core.ed2 import *



class SixLines(Predict):
    '''
    predict by 'six lines' method
    '''

    KEY_ED_DOWN = 'eddown'
    KEY_ED_UP = 'edup'

    KEY_SYMBOL_0 = 'symbol0'
    KEY_SYMBOL_1 = 'symbol1'
    KEY_SYMBOL_2 = 'symbol2'
    KEY_SYMBOL_3 = 'symbol3'
    KEY_SYMBOL_4 = 'symbol4'
    KEY_SYMBOL_5 = 'symbol5'

    KEY_LIST = [
        KEY_ED_DOWN,
        KEY_ED_UP,
        KEY_SYMBOL_0,
        KEY_SYMBOL_1,
        KEY_SYMBOL_2,
        KEY_SYMBOL_3,
        KEY_SYMBOL_4,
        KEY_SYMBOL_5
    ]

    def __init__(self, engine):
        super().__init__()
        self._engine = engine

    def getDictKeyList(self):
        l = super().getDictKeyList()
        l.extend(SixLines.KEY_LIST)
        return l