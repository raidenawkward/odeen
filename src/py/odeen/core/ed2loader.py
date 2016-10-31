# coding = utf-8

import json
import ed2
from ed2 import *


class ED2Loader:
    '''
    load/save ED2s from file
    '''

    ED_INDEX_LIST = [
        [0, '乾'],
        [1, '兑'],
        [2, '离'],
        [3, '震'],
        [4, '巽'],
        [5, '坎'],
        [6, '艮'],
        [7, '坤']
    ]

    def _parseSymbolName(string):
        if string is None:
            return None

        start1 = string.index('）') + 1
        end1 = string.index('上')
        name1 = ''
        for i in range(start1, end1):
            name1 = name1 + string[i]

        start2 = end1 + 1
        end2 = string.index('下', start2 + 1)
        name2 = ''
        for i in range(start2, end2):
            name2 = name2 + string[i]

        index1 = -1
        index2 = -1
        for item in ED2Loader.ED_INDEX_LIST:
            if item[1] == name1:
                index1 = item[0]
            elif item[1] == name2:
                index2 = item[0]

        l = [index1, index2]

        return l

    def loadEd2FromEdDict(filePath, silent=False):
        if filePath is None:
            return None

        fp = open(filePath, 'rb')
        content = fp.read()
        jsonDict = json.loads(content.decode(), encoding='utf-8')
        fp.close()

        ed2list = []

        if silent is False:
            version = jsonDict['version']
            print('loaded ed2 dict from ' + filePath + ', version: ' + version)

        ed2dictList = jsonDict['symbolsdict']
        ed2List = []

        for ed2dict in ed2dictList:
            index = ed2dict['index']
            name = ed2dict['name']
            explain = ed2dict['explain']
            explaintrans = ed2dict['explaintranslate']['CN']
            comment = ed2dict['comment']

            edsList = ED2Loader._parseSymbolName(explain)
            edsstr = str(edsList[0]) + ',' + str(edsList[1])

            ed2 = ED2(id=index, name=name, explain=explain, explainTranslation=explaintrans,
            comment=comment, eds=edsstr)

            ed2List.append(ed2)

            print(ed2.toString())

        return ed2List


if __name__ == '__main__':
    ed2list = ED2Loader.loadEd2FromEdDict('eddict')
