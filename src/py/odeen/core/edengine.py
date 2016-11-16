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

    ENGINE_VERSION = '0.4'

    DEF_DATA_PATH = './data'
    DEF_BACKUP_PATH = './backup'
    DEF_ED_FILE_PATH = DEF_DATA_PATH + '/ed'
    DEF_ED2_FILE_PATH = DEF_DATA_PATH + '/ed2'
    DEF_ED_DISTRIBUTE_FOLDER_PATH = DEF_DATA_PATH + '/eddistribute'
    DEF_ED2_DISTRIBUTE_FOLDER_PATH = DEF_DATA_PATH + '/ed2distribute'



    def __init__(self, edDistribute=DEF_ED_DISTRIBUTE_FOLDER_PATH, ed2Distribute=DEF_ED2_DISTRIBUTE_FOLDER_PATH, silent=False):
        self._edList = []
        self._ed2List = []
        self._silent = silent
        self._edDestributePath = edDistribute
        self._ed2DestributePath = ed2Distribute

        if edDistribute is not None:
            self.loadEdFromDistribute(edDistribute)

        if ed2Distribute is not None:
            self.loadEd2ListFromDistribute(ed2Distribute)

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

    def findEd(self, index=-1, symbolList=None, name=None):
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

        if name is not None:
            for ed in edList:
                if ed.getName() == name:
                    return ed

        return None

    def syncEd(self, ed, distributeFolder=DEF_ED_DISTRIBUTE_FOLDER_PATH):
        import os
        if ed is None or distributeFolder is None:
            return

        path = os.path.join(distributeFolder, str(ed.getId()))
        ed.load(path)

    def saveEd(self, ed, distributeFolder=DEF_ED_DISTRIBUTE_FOLDER_PATH):
        import os
        if ed is None or distributeFolder is None:
            return

        path = os.path.join(distributeFolder, str(ed.getId()))
        ed.save(path)

    def saveEdToFile(self, filePath=None, version='0.1'):
        if filePath is None:
            filePath = 'ed.' + time.strftime('%Y%m%d.%H%M%S')

        edList = self.getEdList()
        EDLoader.saveEdToFile(edList, filePath, version)

    def saveEdToDistribute(self, folder=DEF_ED_DISTRIBUTE_FOLDER_PATH):
        import os

        edList = self.getEdList()
        for ed in edList:
            path = os.path.join(folder, str(ed.getId()))
            ed.save(path)
            if self.isSilent() is False:
                print('saved ed ' + str(ed.getId()) + ' to ' + path)

    def loadEdFromDistribute(self, folder=DEF_ED2_DISTRIBUTE_FOLDER_PATH):
        import os

        self._edDestributePath = folder

        edList = self.getEdList()
        edList.clear()

        for i in range(0, 8):
            path = os.path.join(folder, str(i))
            ed = ED()
            ed.load(path)
            edList.append(ed)
            if self.isSilent() is False:
                print('load ed ' + str(ed.getId()) + ' from ' + path)

        return edList

    # methods for ed2
    def loadEd2ListFromFile(self, filePath=DEF_ED2_FILE_PATH, silent=False):
        self._ed2List = ED2Loader.loadEd2ListFromFile(filePath, silent)
        return self.getEdList()

    def loadEd2ListFromDistribute(self, distributeFolder=DEF_ED2_DISTRIBUTE_FOLDER_PATH):
        import os

        self._ed2DestributePath = distributeFolder

        ed2List = self.getEd2List()
        ed2List.clear()

        for i in range(0, 64):
            path = os.path.join(distributeFolder, str(i))
            ed2 = ED2()
            ed2.load(path)
            ed2List.append(ed2)

            if self.isSilent() is False:
                print('load ed2 ' + str(ed2.getId()) + ' from ' + path)

    def getEd2List(self):
        return self._ed2List

    def findEd2(self, index=-1, edIndexList=None, edList=None, symbolList=None, name=None):
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

        if name is not None:
            for ed2 in self.getEd2List():
                if ed2.getName() == name:
                    return ed2

        return None

    def syncEd2(self, ed2, distributeFolder=DEF_ED2_DISTRIBUTE_FOLDER_PATH):
        import os
        if ed2 is None or distributeFolder is None:
            return

        path = os.path.join(distributeFolder, str(ed2.getId()))
        ed2.load(path)

    def saveEd2(self, ed2, distributeFolder=DEF_ED2_DISTRIBUTE_FOLDER_PATH):
        import os
        if ed2 is None or distributeFolder is None:
            return

        path = os.path.join(distributeFolder, str(ed2.getId()))
        ed2.save(path)

    def saveEd2ToFile(self, filePath=None, version = '0.1'):
        if filePath is None:
            filePath = 'ed2.' + time.strftime('%Y%m%d.%H%M%S')

        ed2List = self.getEd2List()
        ED2Loader.saveEd2ToFile(ed2List, filePath, version)

    def saveEd2ListToDistrubute(self, distributePath=DEF_ED2_DISTRIBUTE_FOLDER_PATH):
        import os

        ed2List = self.getEd2List()
        for ed2 in ed2List:
            path = os.path.join(distributePath, str(ed2.getId()))
            ed2.save(path)
            if self.isSilent() is False:
                print('save ed2 ' + str(ed2.getId()) + ' to ' + path)

    def backupData(self, src=DEF_DATA_PATH, dst=None):
        import zipfile
        import os
        import time

        if dst is None:
            dst = EDEngine.DEF_BACKUP_PATH
            dst = dst + '/data.' + str(time.time()) + '.bak.zip'

        dstDir = os.path.dirname(dst)
        os.makedirs(dstDir, exist_ok=True)

        if self.isSilent() is False:
            print('creating backup file ' + dst)

        z = zipfile.ZipFile(dst, 'w', zipfile.zlib.DEFLATED)

        filelist = []
        if os.path.isfile(src):
            filelist.append(src)
            z.write(src)
        else :
            for root, dirs, files in os.walk(src):
                for name in files:
                    filelist.append(os.path.join(root, name))
                    if self.isSilent() is False:
                        print('writting zip file ' + os.path.join(root, name))
                    z.write(os.path.join(root, name))

        z.close()





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