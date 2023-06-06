from .. import *
import tkinter as tk
from tkinter import ttk
class TkBaseWidget(PUINode):
    def __init__(self, layout=None, side=None):
        super().__init__()
        self.layout_type = layout
        self.side = side

    @property
    def tkparent(self):
        parent = self.parent
        while not isinstance(parent, TkBaseWidget):
            parent = parent.parent
            if parent==parent.parent:
                return None
        return parent

    def destroy(self, direct):
        if self.ui:
            self.ui.destroy() # tk's destroy
            self.ui = None