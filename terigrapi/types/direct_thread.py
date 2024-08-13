from .base import MutableInstagramObject
from .user import User
from .last_seen import LastSeen
from .direct_item import DirectItem


class DirectThread(MutableInstagramObject):
    has_older: bool
    has_newer: bool
    pending: bool
    items: list[DirectItem]
    canonical: bool
    thread_id: str
    thread_v2_id: str
    users: list[User]
    viewer_id: int
    last_activity_at: int
    muted: bool
    vc_muted: bool
    encoded_server_data_info: str
    admin_user_ids: list[int]
    approval_required_for_new_members: bool
    archived: bool
    thread_has_audio_only_call: bool
    pending_user_ids: list[int]
    last_seen_at: dict[str, LastSeen]
    relevancy_score: int
    relevancy_score_expr: int
    oldest_cursor: str
    newest_cursor: str
    inviter: User
    thread_languages: dict[str, str] # paris user_id to language
    last_permanent_item: DirectItem | None = None

