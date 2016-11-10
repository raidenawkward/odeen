# coding = utf-8

import sys
import threading

from core.ed import ED
from core.ed2 import ED2
from core.edengine import EDEngine
from predict.sixlines.sixlines import SixLines
from predict.predict import Predict
from predict.ui.console.displayhelper import DisplayHelper
from predict.ui.console.progress import ProgressBar
from predict.ui.console.cycle import Cycle




class Launcher:
    '''
    UI entrance for Six Lines Predict
    '''

    DEF_NAME = 'NOBODY'
    DEF_PREDICT_ISSUE = 'ANYTHING'

    LOOP_STOP_SIGN = [
        'exit',
        'quit',
        'done',
        'finish',
        'e',
        'q'
    ]

    def __init__(self, edengine=None, predict=None, silent=False, consoleTag=None):
        self._edengine = edengine
        self._predict = predict
        self._silent = silent
        self._consoleTag = consoleTag

        # UI items
        self._progressBar = None
        self._cycle = None

        # context items
        self._userName = Launcher.DEF_NAME
        self._predictIssue = Launcher.DEF_PREDICT_ISSUE

    def getEdEngine(self):
        return self._edengine

    def getPredict(self):
        return self._predict

    def isSilent(self):
        return self._silent

    def getConsoleTag(self):
        return self._consoleTag

    def _prepare(self):
        if self.getPredict() is None:
            if self.getEdEngine() is None:
                self._edengine = EDEngine(silent=self.isSilent())
            self._predict = SixLines(self.getEdEngine())

    def _printMessage(self, message='', tag=None, newLine=True):
        if self.isSilent():
            return

        if tag is None:
            tag = self.getConsoleTag()

        DisplayHelper.displayLine(message, tag, newLine)


    class CyclingThread(threading.Thread):
        def __init__(self, ticks=10, interval=0.5):
            super().__init__()
            self.cycle = Cycle(ticks=ticks, interval=interval)

        def run(self):
            self.cycle.start()

        def stop(self):
            self.cycle.stop()

    def startCycling(self, ticks=10, interval=0.5, inThread=False):
        if inThread:
            thread = Launcher.CyclingThread()
            thread.start()
        else:
            self.cycle = Cycle(ticks=ticks, interval=interval)
            self.cycle.start()

    def __formatDictList(l):
        if l is None:
            return ''

        string = ''
        for i in l:
            if i == ED.YIN:
                string = string + '阴'
            elif i == ED.YANG:
                string = string + '阳'
            else:
                string = 'error'
                return string

        return string

    def _formatEd2(self, ed2):
        if ed2 is None:
            return "未找到"

        string = ''

        # mark
        string = string + str(ed2.getSymbolMark()) + '\n'
        # name
        string = string + str(ed2.getName()) + '\n'
        # explain
        string = string + str(ed2.getExplain()) + '\n'
        # explain translation
        string = string + str(ed2.getExplainTranslation()) + '\n'
        # comment
        string = string + str(ed2.getComment()) + '\n'

        return string

    def _savePredictToPath(self, predict, path):
        if predict is None:
            self._printMessage('结果不存在')
            return

        try:
            predict.save(path)
        except:
            self._printMessage('存储失败: ' + path)
            return

        self._printMessage('存储完成: ' + path)

    def _startPredictLoop(self):
        predict = self.getPredict()
        if predict is None:
            return

        while True:
            if predict.isStarted() is False:
                userName = input('输入你的姓名(' + str(self._userName) + '):')
                if userName is not None and len(userName) > 0:
                    self._userName = userName
                    predict.setPredictor(userName)

                predictIssue = input('输入你的目的(' + str(self._predictIssue) + '):')
                if predictIssue is not None and len(predictIssue) > 0:
                    self._predictIssue = predictIssue
                    predict.setPredictIssue(predictIssue)

                title = '你好 ' + str(self._userName) + ', 下面看看[' + str(self._predictIssue) + '] 怎么样:'
                self._printMessage(title)

            if predict.isFinished() is True:
                self._printMessage('这一卦的结果是:')

                ed2 = predict.getResult()
                formatted = self._formatEd2(ed2)
                self._printMessage(formatted)

                userInput = input('继续(ENTER/SAVE):')
                if Launcher.LOOP_STOP_SIGN.count(str(userInput).lower()) > 0:
                    predict.reset()
                    break;
                elif 'save' == str(userInput).lower():
                    savePath = input('路径:')
                    self._savePredictToPath(predict, savePath)
                    predict.reset()
                else:
                    predict.reset()
                    continue

            userInput = input('下一步(ENTER):')
            if Launcher.LOOP_STOP_SIGN.count(str(userInput).lower()) > 0:
                break;

            diceNeedsContinue, diceResult, diceList = predict.dice()
            if diceNeedsContinue is True:
                diceResultStr = "阴" if diceResult == ED.YIN else "阳"
                self._printMessage('这一爻的结果是: ' + diceResultStr + ' (' + Launcher.__formatDictList(diceList) + ')')


        self._printMessage('结束')

    def launch(self):
        self._printMessage('starting..')
        #self.startCycling()
        self._prepare()
        self._startPredictLoop()

