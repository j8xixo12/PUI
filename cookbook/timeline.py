from .config import *

@PUI
def TimelineViewExample():
    from datetime import datetime

    with TimelineView(ttl_sec=1):
        Label(f"{datetime.now().replace(microsecond=0)}")
