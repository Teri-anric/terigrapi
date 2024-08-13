from httpx import AsyncClient, Response
from terigrapi.client.utils import generate_signature, dumps
from terigrapi.enum import ClientApiType
import httpx
import orjson
from .base import BaseSession
import httpx
import orjson
import zstandard as zstd
from httpx import (
    Request,
    CloseError,
    ConnectError,
    ConnectTimeout,
    CookieConflict,
    DecodingError,
    HTTPError,
    HTTPStatusError,
    InvalidURL,
    LocalProtocolError,
    NetworkError,
    PoolTimeout,
    ProtocolError,
    ProxyError,
    ReadError,
    ReadTimeout,
    RemoteProtocolError,
    RequestError,
    TimeoutException,
    TooManyRedirects,
    TransportError,
    UnsupportedProtocol,
    WriteError,
    WriteTimeout,
)
from httpx._client import ClientState
from httpx._decoders import SUPPORTED_DECODERS, ContentDecoder


from typing import TYPE_CHECKING, AsyncGenerator, Any
from types import TracebackType
from abc import ABC, abstractmethod
from terigrapi.methods.base import InstagramMethod, InstagramType, MethodRequestOptions, ReturnBuild
from terigrapi.client.exeptions import (
    ClientJSONDecodeError,
    ClientRequestTimeout,
    ClientUnauthorizedError,
    ClientForbiddenError,
    ClientBadRequestError,
    ClientThrottledError,
    ClientNotFoundError,
    ClientError,
    ClientConnectionError
)
if TYPE_CHECKING:
    from terigrapi.client import Client as InstagramClient
    from .config import SessionConfig



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


class Session(BaseSession):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._client = None
    
    def _clear_dict_none(self, data: dict):
        return {k: v for k, v in data.items() if v}

    @property
    def http_client(self) -> AsyncClient:
        if self._client is None:
            self._client = AsyncClient(
                base_url=self.config.api_url,
                cookies=self._preparate_data(self.config.cookeis),
                **self.config.kwargs
            )
        return self._client
    
    async def _make_request(self, method: InstagramMethod[InstagramType]) -> Response:
        if self.http_client._state is ClientState.UNOPENED:
            await self.http_client.__aenter__()

        request = self.biuld_request(method=method)
        
        return await self.http_client.send(request)

    def response_load(self, method: InstagramMethod[InstagramType], response: Response) -> InstagramType:
        try:
            options = method.__options__
            if isinstance(options.returning, ReturnBuild):
                return options.returning(method, response.headers, response.cookies, response.content)
            
            json_data = orjson.loads(response.content)

            if isinstance(json_data, dict):
                return options.returning(**json_data)
            if isinstance(json_data, list):
                return options.returning(*json_data)
            return options.returning(json_data)
        
        except orjson.JSONDecodeError as e:
            raise ClientJSONDecodeError(
                "JSONDecodeError {0!s} while opening {1!s}".format(e, response.url),
                response=response,
            )

    async def make_request(self, client, method: InstagramMethod[InstagramType]) -> InstagramType:
        response = None
        result = None
        try:
            response = await self._make_request(method)
            result = self.response_load(method, response)
            response.raise_for_status()
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
            raise ClientConnectionError("{} {}".format(e.__class__.__name__, str(e))) from e
    
    def method_dump(self, method: InstagramMethod[InstagramType], *args, **kwargs):
        return self._preparate_data(method.model_dump(*args, **kwargs, by_alias=True, warnings=False))


    def biuld_request(self, method: InstagramMethod[InstagramType]) -> Request:
        options = method.__options__

        kwargs = {}
        kwargs["headers"] = self._clear_dict_none(
            self._preparate_data(self.config.base_headers) | self._preparate_data(options.headers)
        )
        if options.method in ("POST","PUT","PATCH"):
            kwargs["data"] = self.method_dump(method, exclude=options.query_fields)
            kwargs["params"] = self.method_dump(method, include=options.query_fields)
            
            if options.with_signature:
                kwargs["data"] = generate_signature(dumps(kwargs["data"]))
        
        if options.method in ("GET", "DELETE"):
            kwargs["params"] = self.method_dump(method)

        return self.http_client.build_request(options.method, options.endpoint, **kwargs)

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