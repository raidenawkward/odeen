# coding = utf-8

import sys

from core.ed import *
from core.ed2 import *
from core.edengine import *
from predict import *
from predict.sixlines.sixlines import *
from predict.ui.console.launcher import *



VERSION = '1.2'


def displayFullHelp(param=None):
    import os
    print('HELP INFORMATION\n')

    appname = 'odeen'
    if param is not None and param[0] is not None:
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

def displayHelp(param=None, cmd=None):
    cmdStr = None

    if cmd is not None:
        cmdStr = cmd
    elif param is None or len(param) <= 2:
        displayFullHelp(param)
        return
    else:
        cmdStr = param[2]

    for item in CMD_LIST:
        for c in item['cmd']:
            if c == cmdStr:
                displayHelpItem(item)
                return

    displayFullHelp()

def showVersion(param):
    engine = EDEngine(silent=True)
    print('program version: ' + VERSION)
    print('engine version: ' + engine.getVersion())

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

    print(str(key) + ', ' + str(keys))
    string = ''
    string = string + '[' + ed2.getName() + ']\n'
    if key is not None:
        keylist = [key]
        string = ed2.toFormattedString(keys=keylist)
    elif keys is not None and len(keys) > 0:
        string = ed2.toFormattedString(keys=keys)
    else:
        string = ed2.toFormattedString()

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
        showEd2Single(ed2, keys=attrs)
        return

    ed2 = edengine.findEd2(name=str(p1))
    showEd2Single(ed2, keys=attrs)

def editEd(param):
    cmd = 'edited'
    id = None
    name = None
    operation = None
    key = None
    value = None

    paramLen = len(param)
    if paramLen < 5:
        displayHelp(cmd=cmd)
        return

    if paramLen > 2:
        if param[2].isdigit():
            id = int(param[2])
        else:
            name = str(param[2])

    if paramLen > 3:
        operation = str(param[3])

    if paramLen > 4:
        key = str(param[4])

    if paramLen > 5:
        value = str(param[5])

    engine = EDEngine(silent=True)
    ed = None
    if id is not None:
        ed = engine.findEd(index=id)
    elif name is not None:
        ed = engine.findEd(name=name)
    else:
        displayHelp(cmd=cmd)
        return

    if ed is None:
        if id is not None:
            print('ed was not found by id ' + str(id))
        else:
            print('ed was not found by name \'' + str(name) + '\'')

    if operation.lower() == 'add' or operation.lower() == 'a':
        if key is None or value is None:
            displayHelp(cmd=cmd)
            return

        originalValue = ed.getDict().get(key)
        if originalValue is not None:
            print('ed ' + str(ed.getId()) + ' has already carried key \'' + key + '\'')
            return

        ed.getDict()[key] = value

        engine.saveEd(ed)

        print('ed ' + str(ed.getId()) + ' received new attribute:')
        print('\t' + key + ' = ' + str(value))

    elif operation.lower() == 'update' or operation.lower() == 'u':
        if key is None or value is None:
            displayHelp(cmd=cmd)
            return

        originalValue = None
        try:
            originalValue = ed.getDict()[key]
            ed.getDict()[key] = value
        except KeyError:
            print('no attribute was found with key \'' + key + '\'')
            return

        engine.saveEd(ed)

        print('ed ' + str(ed.getId()) + ' updated:')
        print('before: ' + key + ' = ' + str(originalValue))
        print('after: ' + key + ' = ' + str(value))

    elif operation.lower() == 'del' or operation.lower() == 'd':
        if key is None:
            displayHelp(cmd=cmd)
            return

        originalValue = None
        try:
            originalValue = ed.getDict()[key]
            del ed.getDict()[key]
        except KeyError:
            print('no attribute was found with key \'' + key + '\'')
            return

        engine.saveEd(ed)

        print('ed ' + str(ed.getId()) + ' deleted attribute:')
        print('\t' + key + ' = ' + str(originalValue))

    else:
        displayHelp(cmd=cmd)
        return

def editEd2(param):
    cmd = 'edited2'
    id = None
    name = None
    operation = None
    key = None
    value = None

    paramLen = len(param)
    if paramLen < 5:
        displayHelp(cmd=cmd)
        return

    if paramLen > 2:
        if param[2].isdigit():
            id = int(param[2])
        else:
            name = str(param[2])

    if paramLen > 3:
        operation = str(param[3])

    if paramLen > 4:
        key = str(param[4])

    if paramLen > 5:
        value = str(param[5])

    engine = EDEngine(silent=True)
    ed2 = None
    if id is not None:
        ed2 = engine.findEd2(index=id)
    elif name is not None:
        ed2 = engine.findEd2(name=name)
    else:
        displayHelp(cmd=cmd)
        return

    if ed2 is None:
        if id is not None:
            print('ed2 was not found by id ' + str(id))
        else:
            print('ed2 was not found by name \'' + str(name) + '\'')

    if operation.lower() == 'add' or operation.lower() == 'a':
        if key is None or value is None:
            displayHelp(cmd=cmd)
            return

        originalValue = ed2.getDict().get(key)
        if originalValue is not None:
            print('ed2 ' + str(ed2.getId()) + ' has already carried key \'' + key + '\'')
            return

        ed2.getDict()[key] = value

        engine.saveEd2(ed2)

        print('ed2 ' + str(ed2.getId()) + ' received new attribute:')
        print('\t' + key + ' = ' + str(value))

    elif operation.lower() == 'update' or operation.lower() == 'u':
        if key is None or value is None:
            displayHelp(cmd=cmd)
            return

        originalValue = None
        try:
            originalValue = ed2.getDict()[key]
            ed2.getDict()[key] = value
        except KeyError:
            print('no attribute was found with key \'' + key + '\'')
            return

        engine.saveEd2(ed2)

        print('ed2 ' + str(ed2.getId()) + ' updated:')
        print('before: ' + key + ' = ' + str(originalValue))
        print('after: ' + key + ' = ' + str(value))

    elif operation.lower() == 'del' or operation.lower() == 'd':
        if key is None:
            displayHelp(cmd=cmd)
            return

        originalValue = None
        try:
            originalValue = ed2.getDict()[key]
            del ed2.getDict()[key]
        except KeyError:
            print('no attribute was found with key \'' + key + '\'')
            return

        engine.saveEd2(ed2)

        print('ed2 ' + str(ed2.getId()) + ' deleted attribute:')
        print('\t' + key + ' = ' + str(originalValue))

    else:
        displayHelp(cmd=cmd)
        return

def backupData(param):
    engine = EDEngine()
    engine.backupData()

def listEdIds(param):
    keydict = ED.__dict__
    for key in keydict.keys():
        if key.startswith('KEY_') and key != 'KEY_LIST':
            print('ED.' + key + ' = \'' + str(keydict[key]) + '\'')

def listEd2Ids(param):
    keydict = ED2.__dict__
    for key in keydict.keys():
        if key.startswith('KEY_') and key != 'KEY_LIST':
            print('ED2.' + key + ' = \'' + str(keydict[key]) + '\'')




CMD_LIST = [
    {'cmd': ['help', 'h'], 'description': 'show this information', 'func': displayHelp, 'usage': 'help [cmd]'},
    {'cmd': ['version', 'v'], 'description': 'show version', 'func': showVersion, 'usage': None},
    {'cmd': ['backup', 'bd', 'back', 'bac', 'bk'], 'description': 'backup data in distribute folder', 'func': backupData, 'usage': 'backupdata [target]'},
    {'cmd': ['sixline', 'sixlines', 'sl'], 'description': 'start six lines predicting', 'func': sixLinesLaunch, 'usage':None},
    {'cmd': ['showed', 'se'], 'description': 'show ed information', 'func': showEd, 'usage': 'showed [keyword1, keyword2..] (keyword could be: id, name)'},
    {'cmd': ['showed2', 'se2'], 'description': 'show ed2 information', 'func': showEd2, 'usage': 'showed2 [keyword1, keyword2..] (keyword could be: id, name)'},
    {'cmd': ['edited', 'ee'], 'description': 'edit ed dictionary', 'func': editEd, 'usage': 'edited edid operation key [value]\n\t\t\toperation could be: add, del, update'},
    {'cmd': ['edited2', 'ee2'], 'description': 'edit ed2 dictionary', 'func': editEd2, 'usage': 'edited2 ed2id operation key [value]\n\t\t\toperation could be: add, del, update'},
    {'cmd': ['edid', 'eid', 'ei'], 'description': 'list supported ids for ed', 'func': listEdIds, 'usage': None},
    {'cmd': ['ed2id', 'e2id', 'e2i'], 'description': 'list supported ids for ed2', 'func': listEd2Ids, 'usage': None},
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