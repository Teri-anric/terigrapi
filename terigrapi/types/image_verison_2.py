from .base import MutableInstagramObject
from .fallback import Fallback
from .url_info import ImageUrlInfo


class ImageVersions2(MutableInstagramObject):
    candidates: list[ImageUrlInfo]

