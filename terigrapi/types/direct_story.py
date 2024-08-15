from .base import InstagramObject
from .direct_item import DirectItem


class DirectStory(InstagramObject):
    items: list[DirectItem]
    has_newer: bool
    next_cursor: str | None = None
    prev_cursor: str | None = None
    unseen_count: int
    newest_cursor: str | None = None
    uq_seq_id: str | None = None
