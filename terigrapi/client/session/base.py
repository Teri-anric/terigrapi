from typing import TYPE_CHECKING, AsyncGenerator, Any, cast
from types import TracebackType
from abc import ABC, abstractmethod
from terigrapi.client.default import BaseDefault
from .middlewares.manager import RequestMiddlewareManager
from terigrapi.methods.base import InstagramMethod, InstagramType

if TYPE_CHECKING:
    from terigrapi.client import Client
    from .config import SessionConfig


class BaseSession(ABC):
    def __init__(self, client: "Client", config: "SessionConfig"):
        self.client = client
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

    def _preparate_data(self, value):
        if isinstance(value, BaseDefault):
            return value(self.client, self.config)
        if isinstance(value, dict):
            return {k: self._preparate_data(v) for k, v in value.items()}
        if isinstance(value, list):
            return [self._preparate_data(x) for x in value]
        if isinstance(value, set):
            return {self._preparate_data(x) for x in value}
        return value

    @abstractmethod
    async def make_request(
        self, client: "Client", method: InstagramMethod[InstagramType]
    ):
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
    def get_cookies_dict(self):
        """
        Private api return cookies data for save session
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
        method: InstagramMethod[InstagramType],
    ) -> InstagramType:
        # Request middleware
        callback = RequestMiddlewareManager._warp_middlewares(
            method.__options__.middlewares, self.make_request
        )
        # Session middleware
        middleware = self.middleware.wrap_middlewares(callback)
        return cast(InstagramType, await middleware(client=self.client, method=method))
