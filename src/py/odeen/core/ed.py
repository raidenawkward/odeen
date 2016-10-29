# coding = utf-8

import os
import json


class ED:
    '''
    definition for Eight Diagrams
    '''

    YIN = 1
    YANG = 0

    # keys those are used in self._dict
    KEY_ID = 'key_id'
    KEY_NAME = 'key_name'
    KEY_NUMBER = 'key_number'
    KEY_SYMBOL = 'key_symbol'
    KEY_YINYANG = 'key_yinyang'
    KEY_FIVEELEMENT = 'key_fiveelement'
    KEY_NATURE = 'key_nature'
    KEY_TEMPERAMENT = 'key_temperament'
    KEY_FAMILY_RELATIONSHIP = 'key_family_relationship'
    KEY_ANIMAL = 'key_animal'
    KEY_BODY = 'key_body'
    KEY_ORGAN = 'key_organ'
    KEY_EIGHTGATE = 'key_eightgate'
    KEY_DIRECTION_OF_EIGHT_DIAGRAM = 'key_direction_of_eight_diagram'
    KEY_DIRECTION_OF_EIGHT_DIAGRAM_2 = 'key_direction_of_eight_diagram_2'
    KEY_GOOD_OR_ILL = 'key_good_or_ill'

    KEY_LIST = [
        KEY_ID,
        KEY_NAME,
        KEY_NUMBER,
        KEY_SYMBOL,
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

    def __init__(self):
        self._dict = {}
        self._initDict()

    def _initDict(self):
        for key in ED.KEY_LIST:
            self.getDict()[key] = None

    def getDict(self):
        return self._dict

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

    def getSymbol(self):
        return self.getDict()[ED.KEY_SYMBOL]

    def setSymbol(self, symbol):
        self.getDict()[ED.KEY_SYMBOL] = symbol

    def toString(self):
        return json.dumps(self.getDict(), ensure_ascii=False)


if __name__ == '__main__':
    ed = ED()
    print(ed.toString())