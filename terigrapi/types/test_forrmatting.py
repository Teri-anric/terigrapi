from .base import InstagramObject

class TextFormatting(InstagramObject):
    start: int
    end: int
    bold: int
    color: str
    intent: str
    semantic_color: str
