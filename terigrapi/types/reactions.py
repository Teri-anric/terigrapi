from .base import MutableInstagramObject, InstagramObject


class EmojiData(InstagramObject):
    timestamp: int
    client_context: str
    sender_id: int
    emoji: str
    super_react_type: str = "none" 


class Reactions(MutableInstagramObject):
    likes: list[int]
    emojis: list[EmojiData]
    likes_count: int

