# coding = utf-8

import time

from core.dictobj import DictObject
from core.edengine import *
from core.ed import *
from core.ed2 import *


class Predict(DictObject):
    '''
    single predict unit
    '''

    KEY_ID = 'key_id'
    KEY_NAME = 'key_name'
    KEY_CREATED_TIME = 'key_created_time'


    KEY_LIST = [
        KEY_ID,
        KEY_NAME,
        KEY_CREATED_TIME
    ]


    def __init__(self):
        super().__init__()
        self._createdTime = time.time()

    def getDictKeyList(self):
        return Predict.KEY_LIST

    def setCreatedTime(self, time):
        self.getDict()[Predict.KEY_CREATED_TIME] = time

    def getCreatedTime(self):
        return self.getDict()[Predict.KEY_CREATED_TIME]
