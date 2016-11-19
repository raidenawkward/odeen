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
    KEY_EXPLAIN = 'explain'
    KEY_EXPLAIN_TRANSLATION = 'explain_translation'
    KEY_COMMENT = 'comment'
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
        KEY_EXPLAIN,
        KEY_EXPLAIN_TRANSLATION,
        KEY_COMMENT,
        KEY_SYMBOL_LIST,
        KEY_ED2_EXPLAIN_LIST
    ]

    def __init__(self, dictionary=None, id=None, name=None, eds=None, symbol=None, explain=None,
    explainTranslation=None, comment=None):
        super().__init__(dictionary)

        if dictionary is None:
            self.setId(id)
            self.setName(name)
            self.setEds(eds)
            self.setSymbol(symbol)
            self.setExplain(explain)
            self.setExplainTranslation(explainTranslation)
            self.setComment(comment)

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

    def setExplain(self, explain):
        self.getDict()[ED2.KEY_EXPLAIN] = explain

    def getExplain(self):
        return self.getDict()[ED2.KEY_EXPLAIN]

    def setExplainTranslation(self, trans):
        self.getDict()[ED2.KEY_EXPLAIN_TRANSLATION] = trans

    def getExplainTranslation(self):
        return self.getDict()[ED2.KEY_EXPLAIN_TRANSLATION]

    def setComment(self, comment):
        self.getDict()[ED2.KEY_COMMENT] = comment

    def getComment(self):
        return self.getDict()[ED2.KEY_COMMENT]

    def getSymbolMark(self):
        symbol = self.getDict()[ED2.KEY_SYMBOL]
        mark = ''
        mark = mark + ('- -' if symbol[5] == '1' else '---') + '\n'
        mark = mark + ('- -' if symbol[4] == '1' else '---') + '\n'
        mark = mark + ('- -' if symbol[3] == '1' else '---') + '\n'
        mark = mark + ('- -' if symbol[2] == '1' else '---') + '\n'
        mark = mark + ('- -' if symbol[1] == '1' else '---') + '\n'
        mark = mark + ('- -' if symbol[0] == '1' else '---')
        return mark

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

        if keys is None or keys.count(ED2.KEY_EDS) > 0:
            eds = self.getDict()[ED2.KEY_EDS]
            string = string + 'eds: ' + eds + ' (down, up)\n'
            finishedKeys.append(ED2.KEY_EDS)

        if keys is None or keys.count(ED2.KEY_ED2_EXPLAIN_LIST) > 0:
            explainList = self.getDict()[ED2.KEY_ED2_EXPLAIN_LIST]
            if explainList is not None:
                string = string + 'explain list:\n\n'

                for explainDict in explainList:
                    string = string + 'explain ' + str(explainList.index(explainDict)) + ':\n'
                    for key in explainDict.keys():
                        string = string + '' + key + ': ' + str(explainDict.get(key)) + '\n'

            finishedKeys.append(ED2.KEY_ED2_EXPLAIN_LIST)

        if keys is None or keys.count(ED2.KEY_SYMBOL_LIST) > 0:
            symbolList = self.getDict().get(ED2.KEY_SYMBOL_LIST)
            if symbolList is not None:
                string = string + '\nsymbol list:\n\n'

                for symbolDict in symbolList:
                    string = string + '' + str(symbolList.index(symbolDict)) + ':\n'
                    for key in symbolDict.keys():
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
