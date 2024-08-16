from .base import InstagramObject


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