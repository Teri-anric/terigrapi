from .base import InstagramObject
from .media_share import MediaShare
from .action_log import ActionLog
from .reactions import Reactions

class DirectItem(InstagramObject):
    item_id: str
    user_id: int
    timestamp: int
    item_type: str
    media_share: MediaShare | None = None
    media: dict = None
    text: str | None = None
    action_log: ActionLog | None = None
    client_context: str
    show_forward_attribution: bool
    forward_score: int | None = None
    is_shh_mode: bool
    is_sent_by_viewer: bool
    reactions: Reactions | None = None
    tq_seq_id: int = None
    uq_seq_id: int
