# coding = utf-8


from core.ed import *
from core.ed2 import *
from core.edengine import *
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





if __name__ == '__main__':
    testEngine()