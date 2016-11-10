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
    KEY_EXPLAIN = 'explain'
    KEY_EXPLAIN_TRANSLATION = 'explain_translation'
    KEY_COMMENT = 'comment'

    KEY_LIST = [
        KEY_ID,
        KEY_NAME,
        KEY_EDS,
        KEY_SYMBOL,
        KEY_EXPLAIN,
        KEY_EXPLAIN_TRANSLATION,
        KEY_COMMENT
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




if __name__ == '__main__':
    ed2 = ED2()
    print(ed2.toString())
