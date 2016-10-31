# coding = utf-8

from ed import *
from ed2 import *

from edloader import *
from ed2loader import *


class EDEngine:
    '''
    ED and ED2 information center
    '''

    DEF_ED_FILE_PATH = './ed'
    DEF_ED2_FILE_PATH = './ed2'


    def __init__(self, edFilePath=DEF_ED_FILE_PATH, ed2FilePath=DEF_ED2_FILE_PATH):
        self._edList = []
        self._ed2List = []

        if edFilePath is not None:
            self.loadEdListFromFile(edFilePath, silent=True)

        if ed2FilePath is not None:
            self.loadEd2ListFromFile(ed2FilePath, silent=True)

    def loadEdListFromFile(self, filePath=DEF_ED_FILE_PATH, silent=False):
        self._edList = EDLoader.loadEdListFromFile(filePath, silent)
        return self.getEdList()

    def getEdList(self):
        return self._edList

    def findEd(self, index=-1):
        edList = self.getEdList()
        if index >= 0 and index < len(edList):
            return edList[index]

        return None

    def loadEd2ListFromFile(self, filePath=DEF_ED2_FILE_PATH, silent=False):
        self._ed2List = ED2Loader.loadEd2ListFromFile(filePath, silent)
        return self.getEdList()

    def getEd2List(self):
        return self._ed2List

    def findEd2(self, index=-1):
        ed2List = self.getEd2List()
        if index >= 0 and index < len(ed2List):
            return ed2List[index]

        return None




if __name__ == '__main__':
    engine = EDEngine()
    edList = engine.getEdList()
    for ed in edList:
        print(ed.getName())

    ed2list = engine.getEd2List()
    for ed2 in ed2list:
        print('' + str(ed2.getId()) + ', ' + ed2.getName())
        print(ed2.getExplain())