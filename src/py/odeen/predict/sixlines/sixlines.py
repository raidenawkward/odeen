# coding = utf-8

import sys

from predict.predict import *
from core.edengine import *
from core.ed import *
from core.ed2 import *




class SixLines(Predict):
    def __init__(self, engine):
        super().__init__(engine)