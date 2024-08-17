from .friendship_status import FriendshipStatus
from .base import MutableInstagramObject
from .shorts_mixin import UserShortsMixin

class User(MutableInstagramObject, UserShortsMixin):
    id: str = None
    pk_id: str
    pk: int
    username: str
    full_name: str
    is_private: bool
    profile_pic_url: str
    profile_pic_id: str | None = None
    friendship_status: FriendshipStatus | None = None
    account_badges: list = None
    has_anonymous_profile_picture: bool = False
    is_unpublished: bool = False
    is_favorite: bool = False
    latest_reel_media: int | None = None
    has_highlight_reels: bool = False
    has_primary_country_in_feed: bool = False
    has_primary_country_in_profile: bool = False
    short_name: str = None
    is_verified: bool
    interop_messaging_user_fbid: int
    fbid_v2: int
    has_ig_profile: bool = None
    interop_user_type: int = None
    is_using_unified_inbox_for_direct: bool = None
    is_eligible_for_rp_safety_notice: bool = None
    is_eligible_for_igd_stacks: bool = None
    is_creator_agent_enabled: bool = None
    biz_user_inbox_state: int = None
    third_party_downloads_enabled: int = None
    wa_eligibility: int = None
    wa_addressable: bool = None
    strong_id__: str
    reachability_status: int = None
    is_active: bool = False
    liked_clips_count: int = 0
