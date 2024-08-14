from pydantic import Field
from ..base import (
    InstagramMethod,
    MethodRequestOptions,
    ClientApiType)
from terigrapi.client.default import DefaultCsrftoken, DefaultFromSettings

__all__ = ["OneTapAppLoginMethod"]


class OneTapAppLoginMethod(InstagramMethod[bool]):
    """
    One Tap Login Emulation
    """

    __options__ = MethodRequestOptions(
        returning=bool,
        method="POST",
        endpoint="/v1/accounts/one_tap_app_login/",
        api_type=ClientApiType.PRIVATE,
    )

    user_id: int
    login_nonce: str

    phone_id: str = DefaultFromSettings("uuids.phone_id")
    adid: str = DefaultFromSettings("uuids.advertising_id")
    guid: str = DefaultFromSettings("uuids.uuid")
    device_id: str = DefaultFromSettings("uuids.uuid")
    csrftoken: str = Field(DefaultCsrftoken(), alias="_csrftoken")
