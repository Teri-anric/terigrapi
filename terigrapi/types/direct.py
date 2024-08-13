from .base import InstagramObject
from .full_user import FullUser
from .direct_inbox import DirectInbox


class Direct(InstagramObject):
    viewer: FullUser
    inbox: DirectInbox
    seq_id: int
    snapshot_at_ms: int
    pending_requests_total: int
    has_pending_top_requests: bool
    unread_pending_requests: int
    status: str
