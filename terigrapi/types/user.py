from .base import MutableInstagramObject, InstagramObject


class FriendshipStatus(InstagramObject):
    following: bool = False
    followed_by: bool = False
    blocking: bool
    muting: bool = False
    is_private: bool = False
    incoming_request: bool = False
    outgoing_request: bool = False
    is_bestie: bool = False
    is_restricted: bool = False
    reachability_status: int | None = None
    is_feed_favorite: bool = False
    is_unavailable: bool = False
    is_messaging_only_blocking: bool = False
    is_messaging_pseudo_blocking: bool = False
    is_viewer_unconnected: bool | None = None


class User(MutableInstagramObject):
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
    wa_eligibility: int = None
    wa_addressable: bool = None
    strong_id__: str
    reachability_status: int = None
    is_active: bool = False