from typing import Literal
from .base import InstagramObject


class Payload(InstagramObject):
    timestamp: str = None
    item_id: str = None
    thread_id: str = None

    client_context: str | None = None
    message: str = None


class DirectResponse(InstagramObject):
    action: str
    status_code: str
    payload: Payload
    message: str = None
    status: Literal["ok", "fail"]


class OkResponse(InstagramObject):
    status: str = "ok"
    status_code: str = 200
