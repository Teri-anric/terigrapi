from .base import MutableInstagramObject
from .direct_cursor import DirectCursor
from .direct_thread import DirectThread


class DirectInbox(MutableInstagramObject):
    threads: list[DirectThread]
    has_older: bool
    unseen_count: int
    unseen_count_ts: int
    oldest_cursor: str | None = None
    prev_cursor: DirectCursor | None = None
    next_cursor: DirectCursor | None = None
    blended_inbox_enabled: bool = False
    pinned_threads: list[DirectThread]

