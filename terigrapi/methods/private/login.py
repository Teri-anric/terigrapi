from typing import Any, MutableMapping
from pydantic import Field

from ..base import InstagramMethod, MethodRequestOptions, ClientApiType, ReturnBuild
from ...client.default import DefaultFromSettings, BaseDefault, JazoestPhoneIdDefault
from ...client.settings import ClientSetting, ClientAuthorization

__all__ = ["AccountLoginMethod"]

class AuthorizationDataReturn(ReturnBuild):
    def __call__(self, method: InstagramMethod, headers: MutableMapping[str, str] = None, cookies: MutableMapping[str, str] = None, content: bytes = None, error: Exception = None):
        authorization_header = headers.get("ig-set-authorization")
        return ClientAuthorization.from_authorization_header(authorization_header)


class AccountLoginMethod(InstagramMethod[ClientAuthorization]):
    """
    Login
    """
    __options__ = MethodRequestOptions(
        returning=AuthorizationDataReturn(),
        method="POST",
        endpoint="/v1/accounts/login/",
        api_type=ClientApiType.PRIVATE,
        headers={
            "Authorization": None
        }
    )

    username: str = DefaultFromSettings("username")
    enc_password: str

    jazoest: str =  JazoestPhoneIdDefault()
    country_codes: str =  DefaultFromSettings("country_code", format='[{{"country_code":"{}","source":["default"]}}]')
    phone_id: str =  DefaultFromSettings("uuids.phone_id")
    adid: str = DefaultFromSettings("uuids.advertising_id")
    guid: str =  DefaultFromSettings("uuids.uuid")
    device_id: str = DefaultFromSettings("uuids.android_device_id")
    google_tokens: str =  "[]"
    login_attempt_count: str =  "0"