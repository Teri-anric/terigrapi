from .base import InstagramObject


class DirectCursor(InstagramObject):
    cursor_timestamp_seconds: int
    cursor_relevancy_score: int
    cursor_thread_v2_id: int

