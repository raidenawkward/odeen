# coding = utf-8

from core.ed import ED
from core.ed2 import ED2
from core.edengine import EDEngine
from core.edupdatehelper import EdUpdateHelper


def addEdSymbol2(oldEd, engine):
    symbol = oldEd.getDict()[ED.KEY_SYMBOL]
    symbol2 = ''

    for i in range(0, len(symbol)):
        if symbol[i] == '0':
            symbol2 = symbol2 + '1'
        else:
            symbol2 = symbol2 + '0'

    print('add symbol 2 ' + str(symbol2) + ' for ' + symbol + ' at ' + oldEd.getName())
    oldEd.getDict()[ED.KEY_SYMBOL2] = symbol2

    return oldEd

def addEd2Symbol2(oldEd2, engine):
    symbol = oldEd2.getDict()[ED2.KEY_SYMBOL]
    symbol2 = ''

    for i in range(0, len(symbol)):
        if symbol[i] == '0':
            symbol2 = symbol2 + '1'
        else:
            symbol2 = symbol2 + '0'

    print('add symbol 2 ' + str(symbol2) + ' for ' + symbol + ' at ' + oldEd2.getName())
    oldEd2.getDict()[ED2.KEY_SYMBOL2] = symbol2

    return oldEd2

def updateEdGoodOrIll(oldEd, engine):
    old = oldEd.getDict()[ED.KEY_GOOD_OR_ILL]
    new = ''
    if old.lower() == 'xiong':
        new = 'ill'
    elif old.lower() == 'ji':
        new = 'good'
    else:
        new = 'general'

    oldEd.getDict()[ED.KEY_GOOD_OR_ILL] = new

    return oldEd

def addEdNumber2(oldEd, engine):
    number = oldEd.getDict()[ED.KEY_NUMBER]
    number2 = 7 - number
    oldEd.getDict()[ED.KEY_NUMBER2] = number2

    return oldEd

def removeEd2UnusedFieleds(oldEd2, engine):
    del oldEd2.getDict()[ED2.KEY_EXPLAIN]
    del oldEd2.getDict()[ED2.KEY_EXPLAIN_TRANSLATION]
    del oldEd2.getDict()[ED2.KEY_COMMENT]

    return oldEd2




if __name__ == '__main__':
    engine = EDEngine()
    helper = EdUpdateHelper(engine)
    helper.updateEd(addEdSymbol2)
    helper.save()