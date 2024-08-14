from httpx import AsyncClient, Response
from .base import BaseSession
import zstandard as zstd
from httpx import ConnectError, DecodingError, HTTPError, ReadError
from httpx._client import ClientState
from httpx._decoders import SUPPORTED_DECODERS, ContentDecoder


from typing import TYPE_CHECKING, AsyncGenerator, Any
from terigrapi.methods.base import InstagramMethod, InstagramType
from terigrapi.client.exeptions import (
    ClientRequestTimeout,
    ClientUnauthorizedError,
    ClientForbiddenError,
    ClientBadRequestError,
    ClientThrottledError,
    ClientNotFoundError,
    ClientError,
    ClientConnectionError,
)

from .types import Response as ResponseModel

if TYPE_CHECKING:
    from terigrapi.client import Client as InstagramClient


class ZstdDecoder(ContentDecoder):
    def __init__(self) -> None:
        self.decompressor = zstd.ZstdDecompressor().decompressobj()

    def decode(self, data: bytes) -> bytes:
        # TODO: optimization
        if not data:
            return b""
        data_parts = [self.decompressor.decompress(data)]
        while self.decompressor.eof and self.decompressor.unused_data:
            unused_data = self.decompressor.unused_data
            self.decompressor = zstd.ZstdDecompressor().decompressobj()
            data_parts.append(self.decompressor.decompress(unused_data))
        return b"".join(data_parts)

    def flush(self) -> bytes:
        ret = self.decompressor.flush()
        if not self.decompressor.eof:
            raise DecodingError("Zstandard data is incomplete")
        return ret


SUPPORTED_DECODERS["zstd"] = ZstdDecoder


class HttpxSession(BaseSession):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._client = None

    def _clear_dict_none(self, data: dict):
        return {k: v for k, v in data.items() if v}

    @property
    def http_client(self) -> AsyncClient:
        if self._client is None or self._client._state is ClientState.CLOSED:
            self._client = AsyncClient(
                base_url=self.config.api_url,
                cookies=self.config.cookeis,
                **self.config.kwargs,
            )
        return self._client

    async def _make_request(
        self, client: "InstagramClient", method: InstagramMethod[InstagramType]
    ) -> Response:
        if self.http_client._state is ClientState.UNOPENED:
            await self.http_client.__aenter__()

        request = self.biuld_request(client, method=method)

        return await self.http_client.request(
            request.method, request.url, data=request.data, headers=request.headers
        )

    async def make_request(
        self, client: "InstagramClient", method: InstagramMethod[InstagramType]
    ) -> InstagramType:
        response = None
        result = None
        try:
            http_response = await self._make_request(client, method)
            response = ResponseModel(
                headers=http_response.headers,
                cookies=http_response.cookies,
                content=http_response.content,
                status_code=http_response.status_code,
            )
            result = self.load_response(client, method, response)
            http_response.raise_for_status()
            return result

        except HTTPError as e:
            match getattr(response, "status_code", None):
                case 400:
                    exc = ClientBadRequestError
                case 401:
                    exc = ClientUnauthorizedError
                case 403:
                    exc = ClientForbiddenError
                case 404:
                    exc = ClientNotFoundError
                case 408:
                    exc = ClientRequestTimeout
                case 429:
                    exc = ClientThrottledError
                case _:
                    exc = ClientError
            raise exc(e, response=response, result=result) from e

        except (ConnectError, ReadError) as e:
            raise ClientConnectionError(
                "{} {}".format(e.__class__.__name__, str(e))
            ) from e

    async def close(self):
        if self.http_client and self.http_client._state is ClientState.OPENED:
            await self.http_client.__aexit__()

    async def stream_content(
        self,
        url: str,
        headers: dict[str, Any] = None,
        timeout: int = 30,
        chunk_size: int = 65536,
        raise_for_status: bool = True,
    ) -> AsyncGenerator[bytes, None]:  # pragma: no cover
        yield b""

    def get_cookies_dict(self):
        return dict(self.http_client.cookies)
