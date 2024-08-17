from .base import MutableInstagramObject
from .text_forrmatting import TextFormatting

class ActionLog(MutableInstagramObject):
    description: str
    bold: list[str | dict[str, int]]
    is_reaction_log: bool = False
    text_attributes: list[TextFormatting] = None
