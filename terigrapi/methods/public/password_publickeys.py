from terigrapi.client.exeptions import ClientError
from terigrapi.methods.return_builds import PasswordPublicKeyReturn
from terigrapi.types.password_publickeys import PasswordPublicKey
from ..base import InstagramMethod, MethodRequestOptions, ClientApiType
from ...client.session.middlewares.suppress import SuppressErrorHandler

__all__ = ["GetPasswordPublicKeyMethod"]


class GetPasswordPublicKeyMethod(InstagramMethod[PasswordPublicKey]):
    __options__ = MethodRequestOptions(
        returning=PasswordPublicKeyReturn(),
        method="GET",
        endpoint="https://i.instagram.com/api/v1/qe/sync/",
        api_type=ClientApiType.PUBLIC,
        middlewares=[SuppressErrorHandler(ClientError)]
    )
    pass

