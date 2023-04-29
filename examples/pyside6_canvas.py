import sys
sys.path.append("..")
from PUI import State
from PUI.PySide6 import *


data = State()
class QtExample(QtApplication):
    def __init__(self):
        super().__init__(title="blah", size=(640,480))
        data.var = 50

    def content(self):
        with QtWindow():
            with QtVBox():
                with QtCanvas():
                    QtCanvasText(data.var, data.var/2, f"blah {data.var}")
                    QtCanvasLine(data.var, data.var, data.var*2, data.var*3)
                with QtHBox():
                    QtButton("-", self.on_minus)
                    QtLabel(f"{data.var}")
                    QtButton("+", self.on_plus)

    def on_minus(self):
        data.var -= 1

    def on_plus(self):
        data.var += 1


from PySide6 import QtWidgets
root = QtExample()
root.run()
