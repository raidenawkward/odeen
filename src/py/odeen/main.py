# coding = utf-8

import sys

from core.ed import *
from core.ed2 import *
from core.edengine import *
from predict import *
from predict.sixlines.sixlines import *
from predict.ui.console.launcher import *



def displayFullHelp(param=None):
    import os
    print('HELP INFORMATION\n')

    appname = 'odeen'
    if param is not None or param[0] is not None:
        appname = os.path.basename(param[0])

    print('' + appname + ' cmd [params]\n')
    print('cmd list:')

    for item in CMD_LIST:
        displayHelpItem(item)

def displayHelpItem(item):
    if item is None:
        return

    cmdList = item['cmd']
    str = '' + cmdList[0] + '\t\t' + item['description']
    if len(cmdList) > 1:
        str = str + '\n' + '\t\talias: '
        for i in range(1, len(cmdList)):
            str = str + cmdList[i]
            if i != len(cmdList) - 1:
                str = str + ', '
        str = str + '\n'
    if item['usage'] is not None:
        str = str + '\t\tusage:\n\t\t\t' + item['usage'] + '\n'

    print(str)

def displayHelp(param):
    if param is None or len(param) <= 2:
        displayFullHelp(param)
        return

    cmdStr = param[2]
    for item in CMD_LIST:
        for c in item['cmd']:
            if c == cmdStr:
                displayHelpItem(item)

def sixLinesLaunch(param):
    launcher = Launcher(silent=False)
    launcher.launch()

def showEdSingle(ed, showDict=False, key=None, keys=None):
    if ed is None:
        return

    string = ''
    string = string + '[' + ed.getName() + ']\n'
    if key is not None:
        edDict = ed.getDict()
        string = string + '' + key + ':' + str(edDict[key]) + '\n'
    elif keys is not None and len(keys) > 0:
        edDict = ed.getDict()
        for k in keys:
            string = string + '' + k + ':' + str(edDict[k]) + '\n'
    else:
        edDict = ed.getDict()
        keys = edDict.keys()
        for k in keys:
            string = string + '' + k + ':' + str(edDict[k]) + '\n'

    print(string)

def showEd(param):
    edengine = EDEngine(silent=True)

    attrs = []
    for i in range(3, len(param)):
        attrs.append(param[i])

    if param is None or len(param) <= 2 or (len(param) > 2 and param[2] == 'all'):
        edList = edengine.getEdList()
        for ed in edList:
            showEdSingle(ed, keys=attrs)
        return

    p1 = str(param[2])
    if p1.isdigit():
        ed = edengine.findEd(index=int(p1))
        showEdSingle(ed, keys=attrs)
        return

    ed = edengine.findEd(name=str(p1))

    showEdSingle(ed, keys=attrs)

def showEd2Single(ed2, showDict=False, key=None, keys=None):
    if ed2 is None:
        return

    string = ''
    string = string + '[' + ed2.getName() + ']\n'
    if key is not None:
        ed2Dict = ed2.getDict()
        string = string + '' + key + ':' + str(ed2Dict[key]) + '\n'
    elif keys is not None and len(keys) > 0:
        ed2Dict = ed2.getDict()
        for k in keys:
            string = string + '' + k + ':' + str(ed2Dict[k]) + '\n'
    else:
        ed2Dict = ed2.getDict()
        keys = ed2Dict.keys()
        for k in keys:
            string = string + '' + k + ':' + str(ed2Dict[k]) + '\n'

    print(string)

def showEd2(param):
    edengine = EDEngine(silent=True)

    attrs = []
    for i in range(3, len(param)):
        attrs.append(param[i])

    if param is None or len(param) <= 2 or (len(param) > 2 and param[2] == 'all'):
        ed2List = edengine.getEd2List()
        for ed2 in ed2List:
            showEd2Single(ed2, keys=attrs)
        return

    p1 = str(param[2])
    if p1.isdigit():
        ed2 = edengine.findEd2(index=int(p1))
        showEdSingle(ed2, keys=attrs)
        return

    ed2 = edengine.findEd2(name=str(p1))
    showEdSingle(ed2, keys=attrs)





CMD_LIST = [
    {'cmd': ['help', 'h'], 'description': 'show this information', 'func': displayHelp, 'usage': 'help [cmd]'},
    {'cmd': ['sixline', 'sixlines', 'sl'], 'description': 'start six lines predicting', 'func': sixLinesLaunch, 'usage':None},
    {'cmd': ['showed', 'se'], 'description': 'show ed information', 'func': showEd, 'usage': 'show ed [keyword] (keyword could be: id, name)'},
    {'cmd': ['showed2', 'se2'], 'description': 'show ed2 information', 'func': showEd2, 'usage': 'show ed2 [keyword] (keyword could be: id, name)'},
]

def main(param):
    """
    entrance
    """
    if param is None or len(param) <= 1:
        displayHelp(param)
        return

    cmdStr = param[1]
    cmd = None

    for item in CMD_LIST:
        for c in item['cmd']:
            if c == cmdStr:
                cmd = item

    if cmd is None:
        displayHelp(param)
        return

    cmd['func'](param)




if __name__ == '__main__':
    main(sys.argv)