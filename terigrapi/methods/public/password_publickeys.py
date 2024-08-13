from typing import MutableMapping
from pydantic import Field

from terigrapi.client.exeptions import ClientError
from terigrapi.types.password_publickeys import PasswordPublicKey
from ..base import InstagramMethod, MethodRequestOptions, ClientApiType, ReturnBuild
from ...client.session.middlewares.suppress import SuppressErrorHandler


__all__ = ["GetPasswordPublicKeyMethod"]


class PasswordPublicKeyReturn(ReturnBuild):
    def __call__(self, method: InstagramMethod, headers: MutableMapping[str, str] = None, cookies: MutableMapping[str, str] = None, content: bytes = None, error: Exception = None):
        publickey_id = headers.get("ig-set-password-encryption-key-id")
        publickey = headers.get("ig-set-password-encryption-pub-key")
        return PasswordPublicKey(publickey_id=publickey_id, publickey=publickey)


class GetPasswordPublicKeyMethod(InstagramMethod[PasswordPublicKey]):
    __options__ = MethodRequestOptions(
        returning=PasswordPublicKeyReturn(),
        method="GET",
        endpoint="https://i.instagram.com/api/v1/qe/sync/",
        api_type=ClientApiType.PUBLIC,
        middlewares=[SuppressErrorHandler(ClientError)]
    )
    pass

