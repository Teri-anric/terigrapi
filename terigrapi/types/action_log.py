from .base import MutableInstagramObject

class ActionLog(MutableInstagramObject):
    description: str
    bold: list[str]
    is_reaction_log: bool

