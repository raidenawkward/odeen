# coding = utf-8


from core.ed import *
from core.ed2 import *
from core.edengine import *
from core.edloader import *
from core.ed2loader import *
from predict import *
from predict.sixlines.sixlines import *


def testEngine():
    edengine = EDEngine()
    edlist = edengine.getEdList()
    for ed in edlist:
        print(ed.getName() + ', ' + str(ed.getNumber()) + ', ' + ed.getDict()[ED.KEY_ANIMAL])

    ed2list = edengine.getEd2List()
    for ed2 in ed2list:
        print(ed2.getName())
        print(ed2.getExplain())

def testSixLines():
    edengine = EDEngine()
    predict = SixLines(edengine)
    predict.getSymbolList()[0] = 1
    predict.getSymbolList()[1] = 2
    predict.getSymbolList()[2] = 3
    print(predict.toJson())

    #predict.save()

    #predict.load('Six Lines_1478156824.525063.txt')
    #print(predict.toJson())

    for i in range (0, 6):
        predict.dice()
        print(predict.toJson())


if __name__ == '__main__':
    #testEngine()
    testSixLines()
