from .base import MutableInstagramObject, InstagramObject


class FriendshipStatus(InstagramObject):
    following: bool
    followed_by: bool = False
    blocking: bool
    muting: bool
    is_private: bool
    incoming_request: bool
    outgoing_request: bool
    is_bestie: bool
    is_restricted: bool
    reachability_status: int = None
    is_feed_favorite: bool


class User(MutableInstagramObject):
    pk: int
    username: str
    full_name: str
    is_private: bool
    profile_pic_url: str
    profile_pic_id: str | None = None
    friendship_status: FriendshipStatus | None = None
    account_badges: list
    has_anonymous_profile_picture: bool
    is_unpublished: bool = False
    is_favorite: bool = False
    latest_reel_media: int | None = None
    has_highlight_reels: bool = False
    has_primary_country_in_feed: bool = False
    has_primary_country_in_profile: bool = False
