import random
from pydantic import Field
from ..base import InstagramMethod, MethodRequestOptions, ClientApiType
from ...client.default import DefaultFromSettings, RandIntStringDefault

__all__ = ["GetTimelineFeedMethod"]


class GetTimelineFeedMethod(InstagramMethod[dict]):
    """
    Get your timeline feed

    reason=cold_start_fetch; is_pull_to_refresh="0"
    """

    __options__ = MethodRequestOptions(
        returning=dict,
        method="POST",
        endpoint="/v1/feed/timeline/",
        api_type=ClientApiType.PRIVATE,
        with_signature=False,
        headers={
            "X-Ads-Opt-Out": "0",
            "X-DEVICE-ID": DefaultFromSettings("uuids.uuid"),
            "X-CM-Bandwidth-KBPS": "-1.000",
            "X-CM-Latency": RandIntStringDefault(1, 5),
        },
    )

    phone_id: str = DefaultFromSettings("uuids.phone_id")
    uuid: str = DefaultFromSettings("uuids.uuid")
    token: str = Field(DefaultFromSettings("token"), alias="_csrftoken")
    request_id: str = DefaultFromSettings("uuids.request_id")
    client_session_id: str = DefaultFromSettings("uuids.client_session_id")
    bloks_versioning_id: str = DefaultFromSettings("bloks_versioning_id")
    timezone_offset: int = DefaultFromSettings("timezone_offset")
    battery_level: int = Field(default_factory=lambda: random.randint(25, 100))
    is_charging: int = Field(default_factory=lambda: random.randint(0, 1))
    will_sound_on: int = Field(default_factory=lambda: random.randint(0, 1))
    feed_view_info: str = "[]"

    reason: str = Field(default="pull_to_refresh")
    is_pull_to_refresh: str = Field(default="1")
