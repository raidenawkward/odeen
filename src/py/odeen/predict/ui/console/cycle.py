# coding = utf-8


class Cycle:
    DEF_LIST = [
        '-', '\\', '|', '/'
    ]

    def __init__(self, l=DEF_LIST, interval=1, ticks=20):
        import sys
        import time

        self._index = 0
        self._list = l
        self._out = sys.stdout
        self._interval = interval
        self._isWorking = False
        self._ticks = ticks
        self._currentTicks = 0

    def getOut(self):
        return self._out

    def getInterval(self):
        return self._interval

    def getList(self):
        return self._list

    def getIndex(self):
        return self._index

    def next(self):
        self._index = self._index + 1
        self._currentTicks = self._currentTicks + 1

        if self.getIndex() >= len(self.getList()):
            self._index = 0

        return self.getList()[self.getIndex()]

    def isWorking(self):
        return self._isWorking

    def getTicks(self):
        return self._ticks

    def start(self):
        import time

        self._isWorking = True
        while self.isWorking():
            if self._currentTicks > self.getTicks():
                break

            nextStr = self.next()
            self.getOut().write(nextStr + '\b')
            self.getOut().flush()
            time.sleep(self.getInterval())

    def stop(self):
        self._isWorking = False




if __name__ == '__main__':
    c = Cycle()
    c.start()