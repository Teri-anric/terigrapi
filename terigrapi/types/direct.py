from .base import InstagramObject
from .viewer_user import ViewerUser
from .direct_inbox import DirectInbox


class Direct(InstagramObject):
    viewer: ViewerUser
    inbox: DirectInbox
    seq_id: int
    snapshot_at_ms: int = None
    pending_requests_total: int
    has_pending_top_requests: bool = False
    unread_pending_requests: int
    status: str
