from .base import MutableInstagramObject


class ImageCandidate(MutableInstagramObject):
    width: int
    height: int
    url: str
    scans_profile: str
    estimated_scans_sizes: list[int]

class ImageVersions2(MutableInstagramObject):
    candidates: list[ImageCandidate]

