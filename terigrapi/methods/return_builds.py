from typing import TYPE_CHECKING
from terigrapi.client.session.types import Response
from terigrapi.client.settings import ClientAuthorization
from terigrapi.constants import UNSET
from terigrapi.methods.base import InstagramMethod, ResultBuild
from terigrapi.types.password_publickeys import PasswordPublicKey

if TYPE_CHECKING:
    from terigrapi.client.client import Client


class AuthorizationDataReturn(ResultBuild):
    def __call__(self, client: "Client", method: InstagramMethod, response: Response):
        authorization_header = response.headers.get("ig-set-authorization")
        return ClientAuthorization.from_authorization_header(authorization_header)


class PasswordPublicKeyReturn(ResultBuild):
    def __call__(self, client: "Client", method: InstagramMethod, response: Response):
        publickey_id = response.headers.get("ig-set-password-encryption-key-id")
        publickey = response.headers.get("ig-set-password-encryption-pub-key")
        return PasswordPublicKey(publickey_id=publickey_id, publickey=publickey)


class DataExtractorReturn(ResultBuild):
    __slots__ = ("_returning", "_keys")

    def __init__(self, *keys: str | int, returning: type = UNSET) -> None:
        self._returning = returning
        self._keys = keys

    def __call__(self, client: "Client", method: InstagramMethod, response: Response):
        data = response.json()
        for key in self._keys:
            try:
                data = data[key]
            except (KeyError, TypeError) as e:
                raise ValueError(f"Error key extractor '{key}': {str(e)}") from e

        if self._returning == UNSET:
            return data

        if isinstance(data, dict):
            return self._returning(**data)
        if isinstance(data, list):
            return self._returning(*data)
        return self._returning(data)
