from .base import MutableInstagramObject, InstagramObject


class FriendshipStatus(InstagramObject):
    following: bool
    followed_by: bool
    blocking: bool
    muting: bool
    is_private: bool
    incoming_request: bool
    outgoing_request: bool
    is_bestie: bool
    is_restricted: bool
    reachability_status: int
    is_feed_favorite: bool


class User(MutableInstagramObject):
    pk: int
    username: str
    full_name: str
    is_private: bool
    profile_pic_url: str
    profile_pic_id: str
    friendship_status: FriendshipStatus
    account_badges: list
    has_anonymous_profile_picture: bool
    is_unpublished: bool
    is_favorite: bool
    latest_reel_media: int
    has_highlight_reels: bool
    has_primary_country_in_feed: bool
    has_primary_country_in_profile: bool
