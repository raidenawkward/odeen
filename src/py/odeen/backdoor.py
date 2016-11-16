# coding = utf-8


from core.ed import *
from core.ed2 import *
from core.edengine import *
from core.edloader import *
from core.ed2loader import *
from predict import *
from predict.sixlines.sixlines import *
from predict.ui.console.launcher import *
from predict.ui.console.progress import ProgressBar
from utils.updatemethods import *
from utils.fetched2frombaidubaike import *
from core.edupdatehelper import EdUpdateHelper


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

def testSixLinesLaunch():
    launcher = Launcher(silent=False)
    launcher.launch()

def testProgress():
    import time

    progressBar = ProgressBar()
    for i in range(0, 99):
        progressBar.progress(i)
        time.sleep(0.5)

def updateSymbol2():
    engine = EDEngine()
    helper = EdUpdateHelper(engine)
    helper.updateEd(addEdSymbol2)
    helper.updateEd2(addEd2Symbol2)
    helper.save()

def _updateEdGoodOrIll():
    engine = EDEngine()
    helper = EdUpdateHelper(engine)
    helper.updateEd(updateEdGoodOrIll)
    helper.save()

def _addEdNumber2():
    engine = EDEngine()
    helper = EdUpdateHelper(engine)
    helper.updateEd(addEdNumber2)
    helper.save()

def addEd2SingleSymbolList():
    '''
    fetch ed2 single symbol items from baidu baike
    '''
    engine = EDEngine()
    sourceEntrances = fetchEntrances()
    ed2list = engine.getEd2List()
    okList = []
    failList = []
    for ed2 in ed2list:
        print('\nfetching ' + ed2.getName())

        name = ed2.getName()
        if name == '遯':
            name = '遁'
        ed2url = sourceEntrances[name]
        sourceEd2Dict = fetchEd2Items(ed2url)

        ed2ExplainList = []
        ed2ExplainDict = {}
        if sourceEd2Dict.get('yi_origin') is not None:
            ed2ExplainDict[ED2.KEY_ED2_EXPLAIN_ORIGIN] = sourceEd2Dict.get('yi_origin')
        if sourceEd2Dict.get('yi_translate') is not None:
            ed2ExplainDict[ED2.KEY_ED2_EXPLAIN_TRANSLATE] = sourceEd2Dict.get('yi_translate')
        if sourceEd2Dict.get('yi_explain') is not None:
            ed2ExplainDict[ED2.KEY_ED2_EXPLAIN_COMMENT] = sourceEd2Dict.get('yi_explain')
        ed2ExplainList.append(ed2ExplainDict)
        ed2.setDictValue(ED2.KEY_ED2_EXPLAIN_LIST, ed2ExplainList)

        ed2SymbolList = sourceEd2Dict.get(ED2.KEY_SYMBOL_LIST)
        if ed2SymbolList is not None:
            ed2.setDictValue(ED2.KEY_SYMBOL_LIST, ed2SymbolList)

        print('[' + ed2.getName() + ']' + ', ' + str(ed2.getId()))

        explainList = ed2.getDictValue(ED2.KEY_ED2_EXPLAIN_LIST)
        print('ed2 explain list: ' + str(explainList))

        symbolList = ed2.getDictValue(ED2.KEY_SYMBOL_LIST)
        if symbolList is None:
            print('no symbol list')
        else:
            print('ed2 item' + '(' + str(len(ed2.getDictValue(ED2.KEY_SYMBOL_LIST))) + '):' + str(ed2.getDictValue(ED2.KEY_SYMBOL_LIST)[0].get(ED2.KEY_ED2_SYMBOL_ORIGIN)))

        if explainList is None:
            failList.append(ed2.getName())
        elif symbolList is None:
            failList.append(ed2.getName())
        elif explainList is not None and len(explainList) > 0 and len(symbolList) == 6:
            okList.append(ed2.getName())
        else:
            failList.append(ed2.getName())

        engine.saveEd2(ed2)

    print('succeed list: ' + str(okList))
    print('failed list: ' + str(failList))



if __name__ == '__main__':
    #testEngine()
    #testSixLines()
    #testSixLinesLaunch()
    #testProgress()
    #updateSymbol2()
    #_updateEdGoodOrIll()
    #_addEdNumber2()
    #addEd2SingleSymbolList()
    print(str(ED.__dict__))
