from .base import InstagramObject
from .fallback import Fallback


class ImageUrlInfo(InstagramObject):
    url: str
    width: int | None
    height: int | None
    fallback: Fallback | None = None
    url_expiration_timestamp_us: int | None = None
    scans_profile: str | None = None
    estimated_scans_sizes: list[int] = None

class VideoUrlInfo(InstagramObject):
    id: str = ""
    type: int
