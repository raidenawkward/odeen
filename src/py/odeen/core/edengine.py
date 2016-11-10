# coding = utf-8

import time

from core.ed import *
from core.ed2 import *

from core.edloader import *
from core.ed2loader import *


class EDEngine:
    '''
    ED and ED2 information center
    '''

    ENGINE_VERSION = '0.1'

    DEF_ED_FILE_PATH = './data/ed'
    DEF_ED2_FILE_PATH = './data/ed2'


    def __init__(self, edFilePath=DEF_ED_FILE_PATH, ed2FilePath=DEF_ED2_FILE_PATH, silent=False):
        self._edList = []
        self._ed2List = []
        self._silent = silent

        if edFilePath is not None:
            self.loadEdListFromFile(edFilePath, silent=self.isSilent())

        if ed2FilePath is not None:
            self.loadEd2ListFromFile(ed2FilePath, silent=self.isSilent())

    def getVersion(self):
        return self.ENGINE_VERSION

    def isSilent(self):
        return self._silent

    # methods for ed
    def loadEdListFromFile(self, filePath=DEF_ED_FILE_PATH, silent=False):
        self._edList = EDLoader.loadEdListFromFile(filePath, silent)
        return self.getEdList()

    def getEdList(self):
        return self._edList

    def findEd(self, index=-1, symbolList=None):
        edList = self.getEdList()
        if index >= 0 and index < len(edList):
            return edList[index]

        #print('symbolList: ' + str(symbolList))
        if symbolList is not None:
            length = len(symbolList)
            number = 0
            for i in range(0, length):
                mod = symbolList[i] << length - i - 1
                number = number + mod

            for ed in self.getEdList():
                if ed.getNumber() == number:
                    return ed

        return None

    def saveEdToFile(self, filePath=None, version='0.1'):
        if filePath is None:
            filePath = 'ed.' + time.strftime('%Y%m%d.%H%M%S')

        edList = self.getEdList()
        EDLoader.saveEdToFile(edList, filePath, version)

    # methods for ed2
    def loadEd2ListFromFile(self, filePath=DEF_ED2_FILE_PATH, silent=False):
        self._ed2List = ED2Loader.loadEd2ListFromFile(filePath, silent)
        return self.getEdList()

    def getEd2List(self):
        return self._ed2List

    def findEd2(self, index=-1, edIndexList=None, edList=None, symbolList=None):
        ed2List = self.getEd2List()
        if index >= 0 and index < len(ed2List):
            return ed2List[index]

        if edIndexList is not None:
            for ed2 in self.getEd2List():
                eds = ed2.getEds()
                if edIndexList[0] == eds[0] and edIndexList[1] == eds[1]:
                    return ed2

        if edList is not None:
            for ed2 in self.getEd2List():
                eds = ed2.getEds()
                if edList[0].getId() == eds[1] and edList[1].getId() == eds[0]:
                    return ed2

        if symbolList is not None:
            symbolListDown = []
            symbolListUp = []
            for i in range(0, int(len(symbolList) / 2)):
                symbolListDown.append(symbolList[i])

            for i in range(int(len(symbolList) / 2), len(symbolList)):
                symbolListUp.append(symbolList[i])

            edDown = self.findEd(symbolList=symbolListDown)
            edUp = self.findEd(symbolList=symbolListUp)
            edList = [edDown, edUp]
            return self.findEd2(edList=edList)

        return None

    def saveEd2ToFile(self, filePath=None, version = '0.1'):
        if filePath is None:
            filePath = 'ed2.' + time.strftime('%Y%m%d.%H%M%S')

        ed2List = self.getEd2List()
        ED2Loader.saveEd2ToFile(ed2List, filePath, version)




if __name__ == '__main__':
    engine = EDEngine()
    edList = engine.getEdList()
    for ed in edList:
        print(ed.getName())

    ed2list = engine.getEd2List()
    #for ed2 in ed2list:
        #print('' + str(ed2.getId()) + ', ' + ed2.getName())
        #print(ed2.getExplain())

    ed2 = engine.findEd2(0)
    print(ed2.getName())

    engine.saveEdToFile()
    engine.saveEd2ToFile()