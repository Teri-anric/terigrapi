from typing import TYPE_CHECKING, AsyncGenerator, Any, cast
from types import TracebackType
from abc import ABC, abstractmethod

from terigrapi.client.default import BaseDefault

from .middlewares.manager import RequestMiddlewareManager
from terigrapi.methods import InstagramMethod, ResultBuild
from terigrapi.constants import UNSET, InstagramType
from .types import Request, Response
from .utils import clear_data, ig_dumps, generate_signature

if TYPE_CHECKING:
    from terigrapi.client import Client
    from .config import SessionConfig


class BaseSession(ABC):
    def __init__(self, config: "SessionConfig"):
        self.config = config

        self.middleware = RequestMiddlewareManager()
        for middleware in config.middlewares:
            self.middleware.register(middleware)

    async def __aenter__(self) -> "BaseSession":
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] = None,
        exc_value: BaseException = None,
        traceback: TracebackType = None,
    ) -> None:
        await self.close()

    @abstractmethod
    async def make_request(
        self, client: "Client", method: InstagramMethod[InstagramType]
    ) -> InstagramType:
        """Make request to API"""
        pass

    @abstractmethod
    async def stream_content(
        self,
        url: str,
        headers: dict[str, Any] = None,
        timeout: int = 30,
        chunk_size: int = 65536,
        raise_for_status: bool = True,
    ) -> AsyncGenerator[bytes, None]:  # pragma: no cover
        """
        Stream reader
        """
        yield b""

    @abstractmethod
    def get_cookies_dict(self) -> dict[str]:
        """
        Private api return cookies data for save session | get data from session cookies
        """
        pass

    @abstractmethod
    async def close(self) -> None:  # pragma: no cover
        """
        Close client session
        """
        pass

    async def __call__(
        self,
        client: "Client",
        method: InstagramMethod[InstagramType],
    ) -> InstagramType:
        # Method middleware
        callback = RequestMiddlewareManager._warp_middlewares(
            method.__options__.middlewares, self.make_request
        )
        # Session middleware
        middleware = self.middleware.wrap_middlewares(callback)
        return cast(InstagramType, await middleware(client=client, method=method))

    def prepare_value(self, client: "Client", value):
        if isinstance(value, BaseDefault):
            return value(client, self)
        if isinstance(value, dict):
            return {k: self.prepare_value(client, v) for k, v in value.items()}
        if isinstance(value, list):
            return [self.prepare_value(client, x) for x in value]
        if isinstance(value, set):
            return {self.prepare_value(client, x) for x in value}
        return value

    def method_dump(
        self, client: "Client", method: InstagramMethod[InstagramType], *args, **kwargs
    ):
        return clear_data(
            self.prepare_value(
                client,
                method.model_dump(*args, **kwargs, by_alias=True, warnings=False),
            )
        )

    def biuld_request(
        self, client: "Client", method: InstagramMethod[InstagramType]
    ) -> Request:
        options = method.__options__

        headers = clear_data(
            self.prepare_value(client, self.config.base_headers)
            | self.prepare_value(client, options.headers),
            exclude=(UNSET, None),
        )
        params = None
        data = None
        if options.method in ("GET", "DELETE"):
            params = self.method_dump(client, method, exclude=options.path_fields)
        if options.method in ("POST", "PUT", "PATCH"):
            params = self.method_dump(client, method, include=options.query_fields)
            data = self.method_dump(client, 
                method, exclude=options.query_fields | options.path_fields
            )
            if options.with_signature:  # dump data with instagram signature format
                data = generate_signature(ig_dumps(data))
        # build url
        url = options.endpoint
        if options.path_fields:
            url = url.format(
                **self.method_dump(client, method=method, include=options.path_fields)
            )
        # build Request
        return Request(
            method=options.method, url=url, headers=headers, params=params, data=data
        )

    def load_response(
        self,
        client: "Client",
        method: InstagramMethod[InstagramType],
        response: Response,
    ) -> InstagramType:
        options = method.__options__
        if options.returning is None or options.returning is UNSET:
            return
        if isinstance(options.returning, ResultBuild):
            return options.returning(client, method, response)
        # load json
        json_data = response.json()
        # return model
        if isinstance(json_data, dict):
            return options.returning(**json_data)
        if isinstance(json_data, list):
            return options.returning(*json_data)
        return options.returning(json_data)
