from threading import Timer
from .view import *

class TimelineView(PUINode):
    def __init__(self, ttl_sec):
        super().__init__()
        self.timer = None
        self.ttl_sec = ttl_sec

    def update(self, prev):
        if prev and hasattr(prev, "timer"):
            self.timer = prev.timer
        else:
            self.timer = Timer(self.ttl_sec, self.timer_cb)
            self.timer.start()

    def timer_cb(self):
        if not self.timer:
            return
        node = self
        while node.retired_by:
            node = node.retired_by
        root = node.root
        if not root:
            return
        root.redraw()
        node.timer = Timer(self.ttl_sec, self.timer_cb)
        node.timer.start()

    @property
    def inner(self):
        return self.parent.inner

    @property
    def outer(self):
        if self.children:
            return self.children[0].outer
        return None

    def destroy(self, direct):
        timer = self.timer
        self.timer = None
        if timer:
            timer.cancel()
        super().destroy(direct)

    def addChild(self, idx, child):
        self.parent.addChild(idx, child)

    def removeChild(self, idx, child):
        self.parent.removeChild(idx, child)
