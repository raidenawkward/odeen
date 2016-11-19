# coding = utf-8

import json

from core.dictobj import DictObject


class ED2(DictObject):
    '''
    definition for Zhouyi Diagrams
    '''

    KEY_ID = 'id'
    KEY_NAME = 'name'
    KEY_EDS = 'eds'
    KEY_SYMBOL = 'symbol'
    KEY_SYMBOL2 = 'symbol2'
    KEY_SYMBOL_LIST = 'single_symbol_list'
    KEY_ED2_EXPLAIN_LIST = 'ed2_explain_list'


    # sub items those will not exist in KEY_LIST
    KEY_ED2_SYMBOL_ORIGIN = 'ed2_symbol_origin'
    KEY_ED2_SYMBOL_TRANSLATE = 'ed2_symbol_trans'
    KEY_ED2_SYMBOL_COMMENT = 'ed2_symbol_comment'
    KEY_ED2_SYMBOL_ANALYSE = 'ed2_symbol_analyse'

    KEY_ED2_EXPLAIN_ORIGIN = 'ed2_explain_origin'
    KEY_ED2_EXPLAIN_TRANSLATE = 'ed2_explain_trans'
    KEY_ED2_EXPLAIN_COMMENT = 'ed2_explain_comment'


    KEY_LIST = [
        KEY_ID,
        KEY_NAME,
        KEY_EDS,
        KEY_SYMBOL,
        KEY_SYMBOL2,
        KEY_SYMBOL_LIST,
        KEY_ED2_EXPLAIN_LIST
    ]

    SYMBOL_BIT_NAME = [
        '初',
        '二',
        '三',
        '四',
        '五',
        '上',
    ]


    def __init__(self, dictionary=None, id=None, name=None, eds=None, symbol=None, explain=None,
    explainTranslation=None, comment=None):
        super().__init__(dictionary)

        if dictionary is None:
            self.setId(id)
            self.setName(name)
            self.setEds(eds)
            self.setSymbol(symbol)

    def getDictKeyList(self):
        return ED2.KEY_LIST

    def setId(self, id):
        self.getDict()[ED2.KEY_ID] = id

    def getId(self):
        return self.getDict()[ED2.KEY_ID]

    def setName(self, name):
        self.getDict()[ED2.KEY_NAME] = name

    def getName(self):
        return self.getDict()[ED2.KEY_NAME]

    def setEds(self, edstr=None, up=None, down=None):
        if edstr is None:
            eds = '' + str(up) + ',' + str(down)
            self.getDict()[ED2.KEY_EDS] = eds
        else:
            self.getDict()[ED2.KEY_EDS] = edstr

    def getEds(self):
        """
        UP,DOWN
        """
        edstr = self.getDict()[ED2.KEY_EDS]
        l = edstr.split(',')
        n = []
        for s in l:
            n.append(int(s))
        return n

    def setSymbol(self, symbol):
        self.getDict()[ED2.KEY_SYMBOL] = symbol

    def getSymbol(self):
        return self.getDict()[ED2.KEY_SYMBOL]

    def getSymbolProposalOrNot(self, position=-1):
        symbol = self.getDict()[ED2.KEY_SYMBOL]
        symbolProposalOrNotList = []

        for i in range(0, len(symbol)):
            if i % 2 == 0:
                if str(symbol[i]) == '0':
                    symbolProposalOrNotList.append(True)
                else:
                    symbolProposalOrNotList.append(False)
            else:
                if str(symbol[i]) == '1':
                    symbolProposalOrNotList.append(True)
                else:
                    symbolProposalOrNotList.append(False)

        if position >= 0 and position < len(symbol):
            return symbolProposalOrNotList[position]

        return symbolProposalOrNotList

    def getSymbolMark(self, position=-1, getlist=False):
        symbol = self.getDict()[ED2.KEY_SYMBOL]

        symbolMarkList = []
        for i in range(0, len(symbol)):
            m = '- -' if symbol[i] == '1' else '---'
            symbolMarkList.append(m)

        if getlist is True:
            return symbolMarkList

        if position >= 0 and position < len(symbol):
            return symbolMarkList[position]

        mark = ''

        for i in range(len(symbolMarkList) - 1, -1, -1):
            mark = mark + ('- -' if symbol[i] == '1' else '---') + '\n'

        return mark

    def getSymbolName(self, position):
        pos = None
        name = None
        res = None

        symbolPosName = ED2.SYMBOL_BIT_NAME[position]
        if symbolPosName is None:
            return res

        symbolBit = str(self.getSymbol())[position]
        if symbolBit is None:
            return res

        symbolBitName = None
        if symbolBit == '0':
            symbolBitName = '九'
        else:
            symbolBitName = '六'

        if position == 0 or position == len(self.getSymbol()) - 1:
            res = symbolPosName + symbolBitName
        else:
            res = symbolBitName + symbolPosName

        return res

    def toFormattedString(self, keys=None, showSymbolMark=True):
        string = ''
        finishedKeys = []

        if keys is None or keys.count(ED2.KEY_NAME) > 0:
            string = string + '[' + self.getName() + ']\n'
            finishedKeys.append(ED2.KEY_NAME)

        if keys is None or keys.count(ED2.KEY_ID) > 0:
            string = string + 'id: ' + str(self.getId()) + '\n'
            finishedKeys.append(ED2.KEY_ID)

        if showSymbolMark is True:
            string = string + self.getSymbolMark() + '\n'

        if keys is None or keys.count(ED2.KEY_SYMBOL) > 0:
            string = string + 'symbol: ' + self.getSymbol() + '\n'
            finishedKeys.append(ED2.KEY_SYMBOL)

        if keys is None or keys.count(ED2.KEY_SYMBOL2) > 0:
            string = string + 'symbol2: ' + str(self.getDict().get(ED2.KEY_SYMBOL2)) + '\n'
            finishedKeys.append(ED2.KEY_SYMBOL2)

        if keys is None or keys.count(ED2.KEY_EDS) > 0:
            eds = self.getDict()[ED2.KEY_EDS]
            string = string + 'eds: ' + eds + ' (down, up)\n'
            finishedKeys.append(ED2.KEY_EDS)

        if keys is None or keys.count(ED2.KEY_ED2_EXPLAIN_LIST) > 0:
            explainList = self.getDict()[ED2.KEY_ED2_EXPLAIN_LIST]
            if explainList is not None:
                string = string + '\n** 卦辞解释 **:\n\n'

                for explainDict in explainList:
                    string = string + '[卦辞 ' + str(explainList.index(explainDict)) + ']\n'
                    explainFinishedKeys = []

                    string = string + '[原文]  ' + str(explainDict.get(ED2.KEY_ED2_EXPLAIN_ORIGIN)) + '\n\n'
                    explainFinishedKeys.append(ED2.KEY_ED2_EXPLAIN_ORIGIN)
                    string = string + '[译文]  ' + str(explainDict.get(ED2.KEY_ED2_EXPLAIN_TRANSLATE)) + '\n\n'
                    explainFinishedKeys.append(ED2.KEY_ED2_EXPLAIN_TRANSLATE)
                    string = string + '[注释]  ' + str(explainDict.get(ED2.KEY_ED2_EXPLAIN_ORIGIN)) + '\n\n'
                    explainFinishedKeys.append(ED2.KEY_ED2_EXPLAIN_TRANSLATE)

                    for key in explainDict.keys():
                        if explainFinishedKeys.count(key) == 0:
                            string = string + '' + key + ': ' + str(explainDict.get(key)) + '\n'

            finishedKeys.append(ED2.KEY_ED2_EXPLAIN_LIST)

        if keys is None or keys.count(ED2.KEY_SYMBOL_LIST) > 0:
            symbolList = self.getDict().get(ED2.KEY_SYMBOL_LIST)
            if symbolList is not None:
                string = string + '\n** 爻位 **\n\n'

                for symbolDict in symbolList:
                    pos = symbolList.index(symbolDict)
                    posName = self.getSymbolName(pos)
                    string = string + '[' + str(posName) + ']\n'

                    symbolFinishedKeys = []

                    symbolIndex = symbolList.index(symbolDict)
                    string = string + '' + str(self.getSymbolMark(position=symbolIndex)) + '\n'
                    if self.getSymbolProposalOrNot(symbolIndex):
                        string = string + '当位\n\n'
                    else:
                        string = string + '不当位\n\n'
                    string = string + '[易经原文]  ' + str(symbolDict.get(ED2.KEY_ED2_SYMBOL_ORIGIN)) + '\n\n'
                    symbolFinishedKeys.append(ED2.KEY_ED2_SYMBOL_ORIGIN)
                    string = string + '[易经译文]  ' + str(symbolDict.get(ED2.KEY_ED2_SYMBOL_TRANSLATE)) + '\n\n'
                    symbolFinishedKeys.append(ED2.KEY_ED2_SYMBOL_TRANSLATE)
                    string = string + '[分析]  ' + str(symbolDict.get(ED2.KEY_ED2_SYMBOL_ANALYSE)) + '\n\n'
                    symbolFinishedKeys.append(ED2.KEY_ED2_SYMBOL_ANALYSE)
                    string = string + '[注释]  ' + str(symbolDict.get(ED2.KEY_ED2_SYMBOL_COMMENT)) + '\n\n'
                    symbolFinishedKeys.append(ED2.KEY_ED2_SYMBOL_COMMENT)

                    for key in symbolDict.keys():
                        if symbolFinishedKeys.count(key) == 0:
                            string = string + '' + key + ': ' + str(symbolDict.get(key)) + '\n'
            finishedKeys.append(ED2.KEY_SYMBOL_LIST)

        # the rest of keys
        if  keys is not None:
            for key in keys:
                if finishedKeys.count(key) == 0:
                    string = string + '' + key + ': ' + str(self.getDict().get(key)) + '\n'
        else:
            for key in ED2.KEY_LIST:
                if finishedKeys.count(key) == 0:
                    string = string + '' + key + ': ' + str(self.getDict().get(key)) + '\n'

        return string



if __name__ == '__main__':
    ed2 = ED2()
    print(ed2.toString())
