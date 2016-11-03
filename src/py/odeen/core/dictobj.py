# coding = utf-8

import json

class DictObject:
    '''
    object that contains dict in it
    '''

    def __init__(self, dictionary=None):
        if dictionary is None:
            self._dict = {}
            self.__initDict()
        else:
            self._dict = dictionary

    def getDict(self):
        return self._dict

    def getDictKeyList(self):
        raise NotImplementedError

    def __initDict(self):
        dictKeyList = self.getDictKeyList()
        self._onInitDict(self.getDict(), dictKeyList) 

    def _onInitDict(self, theDict, keyList):
        for key in keyList:
            theDict[key] = ''

    def toJson(self):
        return json.dumps(self.getDict(), ensure_ascii=False)

    def loadFromJson(self, jsonStr):
        if jsonStr is None:
            return

        self._dict = json.loads(jsonStr)