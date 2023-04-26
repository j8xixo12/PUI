from .. import *
from .base import *

from PySide6 import QtWidgets
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QPoint

class PUIQtCanvas(QtWidgets.QWidget):
    def __init__(self, puinode):
        self.puinode = puinode
        super().__init__()

    def paintEvent(self, event):
        qpainter = QPainter()
        qpainter.begin(self)

        for c in self.puinode.children:
            c.draw(qpainter)

        qpainter.end()

class QtCanvas(QtBaseWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = None

    def update(self, prev):
        if prev and hasattr(prev, "ui"):
            self.ui = prev.ui
            self.ui.puinode = self
        else:
            self.ui = PUIQtCanvas(self)
        self.ui.resize(self.layout_width or 0, self.layout_height or 0)
        self.ui.update()

class QtCanvasText(PUINode):
    def __init__(self, x, y, text):
        super().__init__()
        self.x = x
        self.y = y
        self.text = text

    def update(self, prev):
        pass

    def draw(self, qpainter):
        qpainter.drawText(QPoint(int(self.x), int(self.y)), self.text)

class QtCanvasLine(PUINode):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def update(self, prev):
        pass

    def draw(self, qpainter):
        qpainter.drawLine(self.x1, self.y1, self.x2, self.y2)