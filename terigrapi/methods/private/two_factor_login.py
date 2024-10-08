from pydantic import Field

from ..base import InstagramMethod, MethodRequestOptions, ClientApiType
from ..return_builds import AuthorizationDataReturn
from ...client.default import DefaultCsrftoken, DefaultFromSettings
from ...client.settings import ClientAuthorization
from ...utils import generate_str_uuid

__all__ = ["TwoFactorAccountLoginMethod"]

class TwoFactorAccountLoginMethod(InstagramMethod[ClientAuthorization]):
    """
    Two Factory Authentification Login
    """
    __options__ = MethodRequestOptions(
        returning=AuthorizationDataReturn(),
        method="POST",
        endpoint="/accounts/two_factor_login/",
        api_type=ClientApiType.PRIVATE,
    )

    username: str = DefaultFromSettings("username")
    verification_code: str
    two_factor_identifier: str = None

    phone_id: str =  DefaultFromSettings("uuids.phone_id")
    csrftoken: str = Field(DefaultCsrftoken(), alias="_csrftoken")
    waterfall_id: str = Field(default_factory=generate_str_uuid)
    trust_this_device: str = "0"
    guid: str = DefaultFromSettings("uuids.uuid")
    device_id: str = DefaultFromSettings("uuids.android_device_id")
    verification_method: str = "3"