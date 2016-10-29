# coding = utf-8

import json


class ED2:
    '''
    definition for Zhouyi Diagrams
    '''

    KEY_ID = 'key_id'
    KEY_NAME = 'key_name'
    KEY_EDS = 'key_eds'
    KEY_SYMBOL = 'key_symbol'
    KEY_EXPLAIN = 'key_explain'
    KEY_EXPLAIN_TRANSLATION = 'key_explain_translation'
    KEY_COMMENT = 'key_comment'

    KEY_LIST = [
        KEY_ID,
        KEY_NAME,
        KEY_EDS,
        KEY_SYMBOL,
        KEY_EXPLAIN,
        KEY_EXPLAIN_TRANSLATION,
        KEY_COMMENT
    ]

    def __init__(self, dictionary=None):
        if dictionary is None:
            self._dict = {}
            self._initDict()
        else:
            self._dict = dictionary

    def _initDict(self):
        for key in ED2.KEY_LIST:
            self.getDict()[key] = None

    def getDict(self):
        return self._dict

    def getSymbolMark(self):
        symbol = self.getDict()[ED.KEY_SYMBOL]
        mark = ''
        mark = mark + ('- -' if symbol[5] == '1' else '---') + '\n'
        mark = mark + ('- -' if symbol[4] == '1' else '---') + '\n'
        mark = mark + ('- -' if symbol[3] == '1' else '---') + '\n'
        mark = mark + ('- -' if symbol[2] == '1' else '---') + '\n'
        mark = mark + ('- -' if symbol[1] == '1' else '---') + '\n'
        mark = mark + ('- -' if symbol[0] == '1' else '---')
        return mark

    def toString(self):
        return json.dumps(self.getDict(), ensure_ascii=False)

    def loadFromString(self, string):
        if string is None:
            return

        self._dict = json.loads(string)




if __name__ == '__main__':
    ed2 = ED2()
    print(ed2.toString())
