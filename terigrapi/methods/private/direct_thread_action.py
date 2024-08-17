from typing import Literal
from pydantic import Field
from terigrapi.client.default import DefaultFromSettings
from ...types import OkResponse
from ..base import InstagramMethod, MethodRequestOptions, ClientApiType

__all__ = ["DirectThreadActionMethod"]


class DirectThreadActionMethod(InstagramMethod[dict]):
    """
    mute:
        Mute the thread
    unmute:
        Unmute the thread
    unmute_video_call:
        Unmute video call for the thread
    mute_video_call:
        Mute video call for the thread
    mark_unread:
        Mark a thread as unread
    hide:
        Hide (delete) a thread
        When you click delete, Instagram hides a thread
    """

    __options__ = MethodRequestOptions(
        returning=OkResponse,
        method="POST",
        endpoint="/v1/direct_v2/threads/{thread_id}/{action}/",
        api_type=ClientApiType.PRIVATE,
        path_fields={"thread_id", "action"},
    )
    thread_id: int
    action: Literal[
        "hide", "mark_unread", "mute_video_call", "unmute_video_call", "mute", "unmute"
    ]

    uuid: str = Field(DefaultFromSettings("uuids.uuid"), alias="_uuid")
