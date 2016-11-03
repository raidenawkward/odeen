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
    dicstr = '{\"key_number\": 123, \"key_good_or_ill\": null, \"key_family_relationship\": null, \"key_symbol\": null, \"key_body\": null, \"key_yinyang\": null, \"key_organ\": null, \"key_fiveelement\": null, "key_animal": null, "key_id": null, "key_eightgate": null, "key_nature": null }'
    ed.loadFromJson(dicstr)
    #print(ed.toString())