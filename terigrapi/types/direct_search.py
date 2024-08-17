from .base import MutableInstagramObject, InstagramObject
from .user import User

class RankedRecipient(InstagramObject):
    user: User

class DirectSearch(MutableInstagramObject):
    ranked_recipients: list[RankedRecipient]
    expires: int
    filtered: bool
    request_id: str
    rank_token: str
    status: str
