from typing import Dict
from pydantic import Field
from ..base import (
    InstagramMethod,
    MethodRequestOptions,
    ClientApiType,
)
from ...client.default import DefaultFromSettings

__all__ = ["GetReelsTrayFeedMethod"]


class GetReelsTrayFeedMethod(InstagramMethod[Dict]):
    """
    Get your reels tray feed
    """

    __options__ = MethodRequestOptions(
        returning=dict,
        method="GET",
        endpoint="/v1/feed/reels_tray/",
        api_type=ClientApiType.PRIVATE,
    )

    reason: str = "pull_to_refresh"

    supported_capabilities_new: str = DefaultFromSettings(
        "config.SUPPORTED_CAPABILITIES"
    )
    timezone_offset: str = DefaultFromSettings("timezone_offset")
    tray_session_id: str = DefaultFromSettings("uuids.tray_session_id")
    request_id: str = DefaultFromSettings("uuids.request_id")
    latest_preloaded_reel_ids: str = "[]"
    page_size: int = 50
    uuid: str = DefaultFromSettings("uuids.uuid")
    # token: str = Field(DefaultFromSettings("token"), alias="_csrftoken")
