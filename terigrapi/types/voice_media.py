

from typing import Literal

from terigrapi.enum import MediaType
from .media import Media
from  .base import InstagramObject

class VoiceMedia(InstagramObject):
    media: Media
    seen_user_ids: list[int]
    seen_count: int
    is_shh_mode: bool
    view_mode: Literal["permanent"]
    replay_expiring_at_us: None