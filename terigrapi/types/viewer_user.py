from .base import MutableInstagramObject
from .shorts_mixin import UserShortsMixin

class ViewerUser(MutableInstagramObject, UserShortsMixin):
    id: str
    pk: int
    pk_id: str
    full_name: str
    is_private: bool
    fbid_v2: int
    allowed_commenter_type: str
    reel_auto_archive: str
    has_onboarded_to_text_post_app: bool
    third_party_downloads_enabled: int
    strong_id__: str
    is_using_unified_inbox_for_direct: bool
    profile_pic_id: str
    profile_pic_url: str
    is_verified: bool
    username: str
    has_anonymous_profile_picture: bool
    all_media_count: int | None = None
    account_badges: list[str]
    interop_messaging_user_fbid: int
    biz_user_inbox_state: int
    wa_addressable: bool
    wa_eligibility: int
    has_encrypted_backup: bool

