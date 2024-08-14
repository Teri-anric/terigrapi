from .base import MutableInstagramObject

class ActionLog(MutableInstagramObject):
    description: str
    bold: list[str | dict[str, int]]
    is_reaction_log: bool = False

