from .short_user import ShortUser
from .base import InstagramObject


class MediaCaption(InstagramObject):
    pk: int
    user_id: int
    text: str
    type: int
    created_at: int
    created_at_utc: int
    content_type: str
    status: str
    bit_flags: int
    did_report_as_spam: bool
    share_enabled: bool
    user: ShortUser
    is_covered: bool
    media_id: int
    has_translation: bool
    private_reply_status: int
