from terigrapi.methods.return_builds import AuthorizationDataReturn

from ..base import InstagramMethod, MethodRequestOptions, ClientApiType
from ...client.default import DefaultFromSettings, JazoestPhoneIdDefault
from ...client.settings import ClientAuthorization


__all__ = ["AccountLoginMethod"]

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