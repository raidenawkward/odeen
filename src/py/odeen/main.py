# coding = utf-8


from core.ed import *
from core.ed2 import *
from core.edengine import *
from predict import *
from predict.sixlines.sixlines import *
from predict.ui.console.launcher import *




def sixLinesLaunch():
    launcher = Launcher(silent=False)
    launcher.launch()



if __name__ == '__main__':
    sixLinesLaunch()