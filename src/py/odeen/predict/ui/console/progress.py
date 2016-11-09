# coding = utf-8


class ProgressBar:
    def __init__(self, total=100, block='#', width=100):
        import sys

        self._total = total
        self._block=block
        self._current = 0
        self._width = width
        self._out = sys.stdout

    def getTotal(self):
        return self._total

    def getCurrent(self):
        return self._current

    def getOut(self):
        return self._out

    def getBlock(self):
        return self._block

    def getWidth(self):
        return self._width

    def progress(self, current, total=None):
        if total is None:
            total = self.getTotal()

        self._current = current
        percentage = current / self.getTotal()
        if percentage > 1:
            percentage = 1

        curWidth = int(self.getWidth() * percentage)

        length = curWidth

        for i in range(0, curWidth + 1):
            self.getOut().write(self.getBlock())

        self.getOut().write('\r')
        '''
        for i in range(0, length + 1):
            self.getOut().write('\b')
        self.getOut().flush()
        '''







def testProgress():
    import time

    progressBar = ProgressBar(100, width=10)
    for i in range(0, 20):
        progressBar.progress(i)
        time.sleep(1)


if __name__ == '__main__':
    testProgress()