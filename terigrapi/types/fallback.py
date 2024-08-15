from .base import InstagramObject

class AudioFallback(InstagramObject):
    audio_src: str


class Fallback(InstagramObject):
    url: str