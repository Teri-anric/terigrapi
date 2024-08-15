from typing import Literal
from .base import InstagramObject
from .media import Media

class VisualMedia(InstagramObject):
    media: Media
    expiring_media_action_summary: None = None
    seen_user_ids: list[int]
    seen_count: int
    view_mode: Literal["permanent", "replayable"]
    replay_expiring_at_us: None = None
    playback_duration_secs: int
    reply_type: None = None
    url_expire_at_secs: int
    story_app_attribution: None = None
    tap_models: list