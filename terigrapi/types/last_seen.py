from typing import Any
from .base import MutableInstagramObject


class LastSeen(MutableInstagramObject):
    timestamp: str
    item_id: str
    shh_seen_state: dict[str, Any]
    created_at: str | None = None
