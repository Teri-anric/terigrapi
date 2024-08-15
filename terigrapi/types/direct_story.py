from .base import InstagramObject

class DirectStory(InstagramObject):
    has_newer: bool
    next_cursor: str | None = None
    prev_cursor: str | None = None
    unseen_count: int
    newest_cursor: str | None = None
    uq_seq_id: str | None = None
