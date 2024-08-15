from .base import InstagramObject
from .url_info import ImageUrlInfo

class XmaLink(InstagramObject):
    preview_url: str
    preview_url_info: ImageUrlInfo | None = None
    header_title_text: str | None = None
    title_text: str
    subtitle_text: str
    target_url: str
    xma_layout_type: int
    preview_layout_type: int
    is_sharable: bool
    header_icon_url: str | None = None
    header_icon_url_info: str | None = None
    header_subtitle_text: str | None = None
    preview_media_fbid: str | None = None
    preview_url_mime_type: str | None = None
    xma_template_type: str | None = None
    subtitle_decoration_type: str | None = None
    bottom_icon_url: str | None = None
