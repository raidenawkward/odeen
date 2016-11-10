# coding = utf-8

import time
import json

from core.dictobj import DictObject
from core.edengine import *
from core.ed import *
from core.ed2 import *


class Predict(DictObject):
    '''
    single predict unit
    '''

    KEY_ID = 'id'
    KEY_NAME = 'name'
    KEY_CREATED_TIME = 'created_time'
    KEY_TYPE = 'type'
    KEY_CONCLUSION = 'conclusion'
    KEY_ISSUE = 'issue'
    KEY_PREDICTOR = 'predictor'


    KEY_LIST = [
        KEY_ID,
        KEY_NAME,
        KEY_CREATED_TIME,
        KEY_TYPE,
        KEY_CONCLUSION,
        KEY_ISSUE
    ]


    def __init__(self):
        super().__init__()
        self.setCreatedTime(time.time())

    def getDictKeyList(self):
        return Predict.KEY_LIST

    def setCreatedTime(self, time):
        self.getDict()[Predict.KEY_CREATED_TIME] = time

    def getCreatedTime(self):
        return self.getDict()[Predict.KEY_CREATED_TIME]

    def _generateName(self):
        name = '' + self.getDict()[Predict.KEY_NAME] + '_' + str(self.getCreatedTime()) + '.txt'
        return name

    def setPredictor(self, predictor):
        self.getDict()[Predict.KEY_PREDICTOR] = predictor

    def setPredictIssue(self, issue):
        self.getDict()[Predict.KEY_ISSUE] = issue

    def reset(self):
        pass