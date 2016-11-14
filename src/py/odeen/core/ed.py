# coding = utf-8

import os
import json

from core.dictobj import DictObject

class ED(DictObject):
    '''
    definition for Eight Diagrams
    '''

    YIN = 1
    YANG = 0

    # keys those are used in self._dict
    KEY_ID = 'id'
    KEY_NAME = 'name'
    KEY_NUMBER = 'number'
    KEY_SYMBOL = 'symbol'
    KEY_SYMBOL2 = 'symbol2'
    KEY_YINYANG = 'yinyang'
    KEY_FIVEELEMENT = 'fiveelement'
    KEY_NATURE = 'nature'
    KEY_TEMPERAMENT = 'temperament'
    KEY_FAMILY_RELATIONSHIP = 'family_relationship'
    KEY_ANIMAL = 'animal'
    KEY_BODY = 'body'
    KEY_ORGAN = 'organ'
    KEY_EIGHTGATE = 'eightgate'
    KEY_DIRECTION_OF_EIGHT_DIAGRAM = 'direction_of_eight_diagram'
    KEY_DIRECTION_OF_EIGHT_DIAGRAM_2 = 'direction_of_eight_diagram_2'
    KEY_GOOD_OR_ILL = 'good_or_ill'

    KEY_LIST = [
        KEY_ID,
        KEY_NAME,
        KEY_NUMBER,
        KEY_SYMBOL,
        KEY_SYMBOL2,
        KEY_YINYANG,
        KEY_FIVEELEMENT,
        KEY_NATURE,
        KEY_TEMPERAMENT,
        KEY_FAMILY_RELATIONSHIP,
        KEY_ANIMAL,
        KEY_BODY,
        KEY_ORGAN,
        KEY_EIGHTGATE,
        KEY_DIRECTION_OF_EIGHT_DIAGRAM,
        KEY_DIRECTION_OF_EIGHT_DIAGRAM_2,
        KEY_GOOD_OR_ILL
    ]

    def __init__(self, dictionary=None):
        super().__init__(dictionary)

    def getDictKeyList(self):
        return ED.KEY_LIST

    def getId(self):
        return self.getDict()[ED.KEY_ID]

    def setId(self, id):
        self.getDict()[ED.KEY_ID] = id

    def getName(self):
        return self.getDict()[ED.KEY_NAME]

    def setName(self, name):
        self.getDict()[ED.KEY_NAME] = name

    def getNumber(self):
        return self.getDict()[ED.KEY_NUMBER]

    def setNumber(self, number):
        self.getDict()[ED.KEY_NUMBER] = number

    def getSymbolMark(self):
        symbol = self.getDict()[ED.KEY_SYMBOL]
        mark = ''
        mark = mark + ('- -' if symbol[2] == '1' else '---') + '\n'
        mark = mark + ('- -' if symbol[1] == '1' else '---') + '\n'
        mark = mark + ('- -' if symbol[0] == '1' else '---')
        return mark




if __name__ == '__main__':
    ed = ED()
    dicstr = '{\"number\": 123, \"good_or_ill\": null, \"family_relationship\": null, \"symbol\": null, \"body\": null, \"yinyang\": null, \"organ\": null, \"fiveelement\": null, "animal": null, "id": null, "eightgate": null, "nature": null }'
    ed.loadFromJson(dicstr)
    #print(ed.toString())