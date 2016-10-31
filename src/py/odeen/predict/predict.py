# coding = utf-8

import sys

sys.path.append('..')

from core.edengine import *
from core.ed import *
from core.ed2 import *


class Predict:
    def __init__(self, engine):
        self._engine = engine

    def getEngine(self):
        return self._engine