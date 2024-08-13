from .base import MutableInstagramObject
from .direct_cursor import DirectCursor



class DirectInbox(MutableInstagramObject):
    threads: list
    has_older: bool
    unseen_count: int
    unseen_count_ts: int
    oldest_cursor: str | None = None
    prev_cursor: DirectCursor | None = None
    next_cursor: DirectCursor | None = None
    blended_inbox_enabled: bool = False


