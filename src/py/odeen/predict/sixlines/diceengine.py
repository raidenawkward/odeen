# coding = utf-8

import random


class DiceEngine:
    class Dice:
        def __init__(self):
            pass

        def dice(self):
            return random.randint(0, 1)

    def __init__(self):
        self._diceList = []
        self._installDices()

    def _installDices(self):
        self._diceList.clear()
        for i in range(0, 3):
            self._diceList.append(DiceEngine.Dice())

    def _getDiceList(self):
        return self._diceList

    def _getDiceResult(self, resultList):
        if resultList is None:
            return -1

        if len(resultList) < 3:
            return -1

        count0 = 0
        count1 = 0
        for r in resultList:
            if r == 0:
                count0 = count0 + 1
            elif r == 1:
                count1 = count1 + 1
            else:
                pass

        if count0 == 3:
            return 0

        if count1 == 3:
            return 1

        if count0 < count1:
            return 0

        return 1

    def dice(self):
        diceResults = []
        for d in self._getDiceList():
            diceResults.append(d.dice())

        res = self._getDiceResult(diceResults)
        #print('dice: ' + str(res))
        return (res, diceResults)