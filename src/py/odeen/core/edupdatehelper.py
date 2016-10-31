# coding = utf-8

from edengine import *
from ed import *
from ed2 import *



class EdUpdateHelper:
    '''
    update ed data
    '''

    def __init__(self, engine):
        self._engine = engine

    def updateEd(self, onEdChanged=None):
        """
        onEdChanged(oldEd, engine), returns new ed
        """
        edList = engine.getEdList()
        for i in range(0, len(edList)):
            oldEd = edList[i]
            newEd = onEdChanged(oldEd, engine)
            edList[i] = newEd

    def updateEd2(self, onEd2Changed=None):
        """
        onEd2Changed(oldEd2, engine), returns new ed2
        """
        ed2List = engine.getEd2List()
        for i in range(0, len(ed2List)):
            oldEd2 = ed2List[i]
            newEd2 = onEd2Changed(oldEd2, engine)
            ed2List[i] = newEd2


ED_UPDATE_LIST = [
    [0, '乾', '开'],
    [1, '兑', '惊'],
    [2, '离', '景'],
    [3, '震', '伤'],
    [4, '巽', '杜'],
    [5, '坎', '休'],
    [6, '艮', '生'],
    [7, '坤', '死']
]

if __name__ == '__main__':
    engine = EDEngine()
    edupdatehelper = EdUpdateHelper(engine)

    def updateEdName(oldEd, engine):
        id = oldEd.getId()
        oldName = oldEd.getName()
        newName = ED_UPDATE_LIST[id][1]
        oldEd.setName(newName)

        oldGate = oldEd.getDict()[ED.KEY_EIGHTGATE]
        newGate = ED_UPDATE_LIST[id][2]
        oldEd.getDict()[ED.KEY_EIGHTGATE] = newGate

        print('change name from ' + oldName + ' to ' + newName + ', gate from ' + oldGate + ' to ' + newGate)
        return oldEd


    edupdatehelper.updateEd(updateEdName)
    #engine.saveEdToFile()

    def updateEd2Name(oldEd2, engine):
        oldName = oldEd2.getName()
        newName = oldName
        if oldName.endswith('卦'):
            index = oldName.index('卦')
            newName = oldName[0:index]

        print('change ed2 name from ' + oldName + ' to ' + newName)
        oldEd2.setName(newName)

        return oldEd2

    edupdatehelper.updateEd2(updateEd2Name)
    #engine.saveEd2ToFile()
