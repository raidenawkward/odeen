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

    def getDictValue(self, key, default=None):
        d = self.getDict()
        value = d.get(key)
        if value is not None:
            return value
        else:
            return default

    def setDictValue(self, key, value):
        self.getDict()[key] = value

    def getDictKeyList(self):
        raise NotImplementedError

    def __initDict(self):
        dictKeyList = self.getDictKeyList()
        self._onInitDict(self.getDict(), dictKeyList) 

    def _onInitDict(self, theDict, keyList):
        for key in keyList:
            theDict[key] = None

    def setDict(self, d):
        self._dict = d

    def toJson(self):
        return json.dumps(self.getDict(), ensure_ascii=False)

    def loadFromJson(self, jsonStr):
        if jsonStr is None:
            return

        self._dict = json.loads(jsonStr)

    def save(self, filePath=None):
        if filePath is None:
            filePath = self._generateName()

        jsonStr = self.toJson()
        file = open(filePath, 'wb')
        file.write(jsonStr.encode())
        file.close()

    def load(self, filePath):
        if filePath is None:
            return

        file = open(filePath, 'rb')
        content = file.read()
        jsonDict = json.loads(content.decode(), encoding='utf-8')
        file.close()

        self.setDict(jsonDict)