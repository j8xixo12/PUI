from .. import *
from .base import *

class QtHBox(QtBaseLayout):
    def update(self, prev):
        if prev and hasattr(prev, "ui"):
            self.ui = prev.ui
        else:
            self.ui = QtWidgets.QHBoxLayout()
        super().update(prev)

class QtVBox(QtBaseLayout):
    def update(self, prev):
        if prev and hasattr(prev, "ui"):
            self.ui = prev.ui
        else:
            self.ui = QtWidgets.QVBoxLayout()
        super().update(prev)

class QtSpacerItem(PUINode):
    def update(self, prev):
        if prev and hasattr(prev, "ui"):
            self.ui = prev.ui
        else:
            self.ui = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        super().update(prev)

    def destroy(self):
        self.ui.deleteLater()
        self.ui = None
        super().destroy()
