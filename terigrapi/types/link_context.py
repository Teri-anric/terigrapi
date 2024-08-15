from .base import InstagramObject

class LinkContext(InstagramObject):
    link_url: str
    link_title: str | None = None
    link_summary: str | None = None
    link_image_url: str | None = None
