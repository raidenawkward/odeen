# coding = utf-8

import sys

from core.ed import *
from core.ed2 import *
from core.edengine import *
from predict import *
from predict.sixlines.sixlines import *
from predict.ui.console.launcher import *



def displayFullHelp(param=None):
    print('HELP INFORMATION\n')

    appname = 'odeen'
    if param is None or param[0] is None:
        appname = param[0]

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




CMD_LIST = [
    {'cmd': ['help', 'h'], 'description': 'show this information', 'func': displayHelp, 'usage': 'help [cmd]'},
    {'cmd': ['sixline', 'sixlines', 'sl'], 'description': 'start six lines predicting', 'func': sixLinesLaunch, 'usage':None},
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