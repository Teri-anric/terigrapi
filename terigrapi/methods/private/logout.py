from typing import Any, MutableMapping
from pydantic import Field

from ..base import InstagramMethod, MethodRequestOptions, ClientApiType, ReturnBuild


__all__ = ["AccountLogoutMethod"]


class AccountLogoutMethod(InstagramMethod[dict]):
    """
    Login
    """
    __options__ = MethodRequestOptions(
        returning=dict,
        method="POST",
        endpoint="/v1/accounts/logout/",
        api_type=ClientApiType.PRIVATE
    )

    one_tap_app_login: bool = True