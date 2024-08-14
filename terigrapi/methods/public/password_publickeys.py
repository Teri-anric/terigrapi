from typing import MutableMapping, TYPE_CHECKING
from pydantic import Field


from terigrapi.client.exeptions import ClientError
from terigrapi.client.session.types import Response
from terigrapi.types.password_publickeys import PasswordPublicKey
from ..base import InstagramMethod, MethodRequestOptions, ClientApiType, ResultBuild
from ...client.session.middlewares.suppress import SuppressErrorHandler

if TYPE_CHECKING:
    from terigrapi.client.client import Client

__all__ = ["GetPasswordPublicKeyMethod"]


class PasswordPublicKeyReturn(ResultBuild):
    def __call__(self, client: "Client", method: InstagramMethod, response: Response):
        publickey_id = response.headers.get("ig-set-password-encryption-key-id")
        publickey = response.headers.get("ig-set-password-encryption-pub-key")
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

