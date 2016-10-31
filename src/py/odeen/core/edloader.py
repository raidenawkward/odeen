# coding = utf-8

import ed
from ed import *


class EDLoader:
    '''
    load/save EDs from file
    '''

    def generateEdList():
        edList = []

        # QIAN
        ed = ED()
        ed.getDict()[ED.KEY_ID] = 0
        ed.getDict()[ED.KEY_NAME] = 'QIAN'
        ed.getDict()[ED.KEY_SYMBOL] = '000'
        ed.getDict()[ED.KEY_NUMBER] = 0
        ed.getDict()[ED.KEY_YINYANG] = 0
        ed.getDict()[ED.KEY_FIVEELEMENT] = 'JIN'
        ed.getDict()[ED.KEY_NATURE] = 'TIAN'
        ed.getDict()[ED.KEY_TEMPERAMENT] = 'JIAN'
        ed.getDict()[ED.KEY_FAMILY_RELATIONSHIP] = 'FATHER'
        ed.getDict()[ED.KEY_ANIMAL] = 'HORSE'
        ed.getDict()[ED.KEY_BODY] = 'HEAD'
        ed.getDict()[ED.KEY_ORGAN] = 'BRAIN'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM] = 'S'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM_2] = 'NW'
        ed.getDict()[ED.KEY_EIGHTGATE] = 'KAI'
        ed.getDict()[ED.KEY_GOOD_OR_ILL] = 'JI'
        edList.append(ed.toString())

        # DUI
        ed = ED()
        ed.getDict()[ED.KEY_ID] = 1
        ed.getDict()[ED.KEY_NAME] = 'DUI'
        ed.getDict()[ED.KEY_SYMBOL] = '001'
        ed.getDict()[ED.KEY_NUMBER] = 1
        ed.getDict()[ED.KEY_YINYANG] = 1
        ed.getDict()[ED.KEY_FIVEELEMENT] = 'JIN'
        ed.getDict()[ED.KEY_NATURE] = 'ZE'
        ed.getDict()[ED.KEY_TEMPERAMENT] = 'YUE'
        ed.getDict()[ED.KEY_FAMILY_RELATIONSHIP] = 'YOUNGEST DAUGHTER'
        ed.getDict()[ED.KEY_ANIMAL] = 'GOAT'
        ed.getDict()[ED.KEY_BODY] = 'NOUTH'
        ed.getDict()[ED.KEY_ORGAN] = 'LUNGS'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM] = 'SE'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM_2] = 'W'
        ed.getDict()[ED.KEY_EIGHTGATE] = 'JING|SUPRISE'
        ed.getDict()[ED.KEY_GOOD_OR_ILL] = 'XIONG'
        edList.append(ed.toString())

        # LI
        ed = ED()
        ed.getDict()[ED.KEY_ID] = 2
        ed.getDict()[ED.KEY_NAME] = 'LI'
        ed.getDict()[ED.KEY_SYMBOL] = '010'
        ed.getDict()[ED.KEY_NUMBER] = 2
        ed.getDict()[ED.KEY_YINYANG] = 0
        ed.getDict()[ED.KEY_FIVEELEMENT] = 'HUO'
        ed.getDict()[ED.KEY_NATURE] = 'HUO'
        ed.getDict()[ED.KEY_TEMPERAMENT] = 'LI'
        ed.getDict()[ED.KEY_FAMILY_RELATIONSHIP] = 'MID DAUGHTER'
        ed.getDict()[ED.KEY_ANIMAL] = 'PHEASANT'
        ed.getDict()[ED.KEY_BODY] = 'EYES'
        ed.getDict()[ED.KEY_ORGAN] = 'GALLBLADDER'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM] = 'E'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM_2] = 'S'
        ed.getDict()[ED.KEY_EIGHTGATE] = 'JING|VIEW'
        ed.getDict()[ED.KEY_GOOD_OR_ILL] = 'ZHONGPING'
        edList.append(ed.toString())

        # ZHEN
        ed = ED()
        ed.getDict()[ED.KEY_ID] = 3
        ed.getDict()[ED.KEY_NAME] = 'ZHEN'
        ed.getDict()[ED.KEY_SYMBOL] = '011'
        ed.getDict()[ED.KEY_NUMBER] = 3
        ed.getDict()[ED.KEY_YINYANG] = 1
        ed.getDict()[ED.KEY_FIVEELEMENT] = 'MU'
        ed.getDict()[ED.KEY_NATURE] = 'LEI'
        ed.getDict()[ED.KEY_TEMPERAMENT] = 'DONG'
        ed.getDict()[ED.KEY_FAMILY_RELATIONSHIP] = 'ELDEST SON'
        ed.getDict()[ED.KEY_ANIMAL] = 'DRAGON'
        ed.getDict()[ED.KEY_BODY] = 'FEET'
        ed.getDict()[ED.KEY_ORGAN] = 'HEART'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM] = 'NE'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM_2] = 'E'
        ed.getDict()[ED.KEY_EIGHTGATE] = 'SHANG'
        ed.getDict()[ED.KEY_GOOD_OR_ILL] = 'XIONG'
        edList.append(ed.toString())

        # XUN
        ed = ED()
        ed.getDict()[ED.KEY_ID] = 4
        ed.getDict()[ED.KEY_NAME] = 'XUN'
        ed.getDict()[ED.KEY_SYMBOL] = '100'
        ed.getDict()[ED.KEY_NUMBER] = 4
        ed.getDict()[ED.KEY_YINYANG] = 0
        ed.getDict()[ED.KEY_FIVEELEMENT] = 'MU'
        ed.getDict()[ED.KEY_NATURE] = 'FENG'
        ed.getDict()[ED.KEY_TEMPERAMENT] = 'RU'
        ed.getDict()[ED.KEY_FAMILY_RELATIONSHIP] = 'ELDEST DAUGHTER'
        ed.getDict()[ED.KEY_ANIMAL] = 'COCK'
        ed.getDict()[ED.KEY_BODY] = 'LEGS'
        ed.getDict()[ED.KEY_ORGAN] = 'LIVER'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM] = 'SW'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM_2] = 'SE'
        ed.getDict()[ED.KEY_EIGHTGATE] = 'DU'
        ed.getDict()[ED.KEY_GOOD_OR_ILL] = 'ZHONGPING'
        edList.append(ed.toString())

        # KAN
        ed = ED()
        ed.getDict()[ED.KEY_ID] = 5
        ed.getDict()[ED.KEY_NAME] = 'KAN'
        ed.getDict()[ED.KEY_SYMBOL] = '101'
        ed.getDict()[ED.KEY_NUMBER] = 5
        ed.getDict()[ED.KEY_YINYANG] = 1
        ed.getDict()[ED.KEY_FIVEELEMENT] = 'SHUI'
        ed.getDict()[ED.KEY_NATURE] = 'SHUI'
        ed.getDict()[ED.KEY_TEMPERAMENT] = 'XIAN'
        ed.getDict()[ED.KEY_FAMILY_RELATIONSHIP] = 'MID SON'
        ed.getDict()[ED.KEY_ANIMAL] = 'PIG'
        ed.getDict()[ED.KEY_BODY] = 'EARS'
        ed.getDict()[ED.KEY_ORGAN] = 'KIDNEY'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM] = 'W'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM_2] = 'N'
        ed.getDict()[ED.KEY_EIGHTGATE] = 'XIU'
        ed.getDict()[ED.KEY_GOOD_OR_ILL] = 'JI'
        edList.append(ed.toString())

        # GEN
        ed = ED()
        ed.getDict()[ED.KEY_ID] = 6
        ed.getDict()[ED.KEY_NAME] = 'GEN'
        ed.getDict()[ED.KEY_SYMBOL] = '110'
        ed.getDict()[ED.KEY_NUMBER] = 6
        ed.getDict()[ED.KEY_YINYANG] = 0
        ed.getDict()[ED.KEY_FIVEELEMENT] = 'TU'
        ed.getDict()[ED.KEY_NATURE] = 'SHAN'
        ed.getDict()[ED.KEY_TEMPERAMENT] = 'ZHI'
        ed.getDict()[ED.KEY_FAMILY_RELATIONSHIP] = 'YONGEST SON'
        ed.getDict()[ED.KEY_ANIMAL] = 'DOG'
        ed.getDict()[ED.KEY_BODY] = 'HANDS'
        ed.getDict()[ED.KEY_ORGAN] = 'STOMACH'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM] = 'NW'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM_2] = 'NE'
        ed.getDict()[ED.KEY_EIGHTGATE] = 'SHENG'
        ed.getDict()[ED.KEY_GOOD_OR_ILL] = 'JI'
        edList.append(ed.toString())

        # KUN
        ed = ED()
        ed.getDict()[ED.KEY_ID] = 7
        ed.getDict()[ED.KEY_NAME] = 'KUN'
        ed.getDict()[ED.KEY_SYMBOL] = '111'
        ed.getDict()[ED.KEY_NUMBER] = 7
        ed.getDict()[ED.KEY_YINYANG] = 1
        ed.getDict()[ED.KEY_FIVEELEMENT] = 'TU'
        ed.getDict()[ED.KEY_NATURE] = 'DI'
        ed.getDict()[ED.KEY_TEMPERAMENT] = 'SHUN'
        ed.getDict()[ED.KEY_FAMILY_RELATIONSHIP] = 'MOTHER'
        ed.getDict()[ED.KEY_ANIMAL] = 'CATTLE'
        ed.getDict()[ED.KEY_BODY] = 'ABDOMEN'
        ed.getDict()[ED.KEY_ORGAN] = 'SPLEEN'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM] = 'N'
        ed.getDict()[ED.KEY_DIRECTION_OF_EIGHT_DIAGRAM_2] = 'SW'
        ed.getDict()[ED.KEY_EIGHTGATE] = 'SI'
        ed.getDict()[ED.KEY_GOOD_OR_ILL] = 'XIONG'
        edList.append(ed.toString())

        return edList

    def saveEdToFile(edList, filePath='./ed', version='0.1'):
        root = {}
        root['version'] = version
        root["codec"] = "utf-8"
        root['edlist'] = edList

        jsonStr = json.dumps(root, ensure_ascii=False)

        file = open(filePath, 'wb')
        file.write(jsonStr.encode())
        file.close()

    def loadEdListFromFile(filePath='./ed', silent=False):
        file = open(filePath, 'rb')
        content = file.read()
        jsonDict = json.loads(content.decode(), encoding='utf-8')
        file.close()
        version = jsonDict['version']
        codec = jsonDict['codec']
        edstringlist = jsonDict['edlist']

        if silent is False:
            print('load ed list from ' + filePath + ', version: ' + version + ', codec: ' + codec)

        edlist = []

        for edstring in edstringlist:
            ed = ED()
            ed.loadFromString(edstring)
            edlist.append(ed)

        return edlist

        


if __name__ == '__main__':
    help(EDLoader)
    edList = EDLoader.generateEdList()
    EDLoader.saveEdToFile(edList)
    edList = EDLoader.loadEdListFromFile()

    for ed in edList:
        print(ed.getSymbolMark())
