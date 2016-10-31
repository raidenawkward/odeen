# coding = utf-8

import json
from ed import *
from ed2 import *
from edengine import *


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

        #start1 = string.index('）') + 1
        start1 = string.index('上') - len('上')
        end1 = string.index('上')
        name1 = ''
        for i in range(start1, end1):
            name1 = name1 + string[i]

        #start2 = end1 + 1
        start2 = string.index('下') - len('下')
        end2 = string.index('下', start2 + 1)
        name2 = ''
        for i in range(start2, end2):
            name2 = name2 + string[i]

        index1 = -1
        index2 = -1

        for item in ED2Loader.ED_INDEX_LIST:
            if item[1] == name1:
                index1 = item[0]

            if item[1] == name2:
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

        engine = EDEngine()

        for ed2dict in ed2dictList:
            index = ed2dict['index']
            name = ed2dict['name']
            explain = ed2dict['explain']
            explaintrans = ed2dict['explaintranslate']['CN']
            comment = ed2dict['comment']

            edsList = ED2Loader._parseSymbolName(explain)
            edUp = engine.findEd(edsList[0])
            edDown = engine.findEd(edsList[1])

            #print('' + name + ': ' + str(edsList[0]) + ', ' + str(edsList[1]) + ', ' + explain)

            edsstr = '' + str(edUp.getId()) + ',' + str(edDown.getId())
            symbol = '' + edDown.getDict()[ED.KEY_SYMBOL] + edUp.getDict()[ED.KEY_SYMBOL]

            ed2 = ED2(id=index, name=name, explain=explain, explainTranslation=explaintrans,
            comment=comment, eds=edsstr, symbol=symbol)

            ed2List.append(ed2)

            #print(edUp.getName() + '上' + edDown.getName() + '下')
            #print(ed2.getSymbolMark())

        return ed2List

    def saveEd2ToFile(ed2list, filePath='./ed2', version='0.1'):
        if ed2list is None:
            return

        root = {}
        root['version'] = version
        root["codec"] = "utf-8"

        ed2JsonList = []

        for ed2 in ed2list:
            jsonStr = ed2.toString()
            ed2JsonList.append(jsonStr)

        root['ed2list'] = ed2JsonList

        jsonStr = json.dumps(root, ensure_ascii=False)

        file = open(filePath, 'wb')
        file.write(jsonStr.encode())
        file.close()

    def loadEd2ListFromFile(filePath='./ed2', silent=False):
        file = open(filePath, 'rb')
        content = file.read()
        jsonDict = json.loads(content.decode(), encoding='utf-8')
        file.close()
        version = jsonDict['version']
        codec = jsonDict['codec']
        ed2stringlist = jsonDict['ed2list']

        if silent is False:
            print('load ed2 list from ' + filePath + ', version: ' + version + ', codec: ' + codec)

        ed2list = []

        for ed2string in ed2stringlist:
            ed2 = ED2()
            ed2.loadFromString(ed2string)
            ed2list.append(ed2)

        return ed2list



if __name__ == '__main__':
    ed2list = ED2Loader.loadEd2FromEdDict('eddict')
    #ED2Loader.saveEd2ToFile(ed2list)
    ed2list = ED2Loader.loadEd2ListFromFile()
    for ed2 in ed2list:
        print('' + str(ed2.getId()) + ', ' + ed2.getName())
        print(ed2.getExplain())

