from .base import MutableInstagramObject


class LastSeen(MutableInstagramObject):
    timestamp: str
    item_id: str
    shh_seen_state: dict[str]
    created_at: str | None = None
