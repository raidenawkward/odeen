# coding = utf-8

import sys
import threading

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

    def __init__(self, edengine=None, predict=None, silent=False, consoleTag=None):
        self._edengine = edengine
        self._predict = predict
        self._silent = silent
        self._consoleTag = consoleTag

        # UI items
        self._progressBar = None
        self._cycle = None

        # context items
        self._userName = None

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

    def startCycling(self, ticks=10, interval=0.5):
        thread = Launcher.CyclingThread()
        thread.start()

    def _startPredictLoop(self):
        if self._predict:
            return

        while True:
            userInput = input()

    def launch(self):
        self._printMessage('starting..')
        self._prepare()
        self.startCycling()

        self._userName = input('输入你的姓名(' + str(self._userName) + '):')
        #self._startPredictLoop()

