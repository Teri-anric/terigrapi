from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Protocol, Any


from ....constants import InstagramType


if TYPE_CHECKING:
    from ...client import Client
    from terigrapi.methods.base import InstagramMethod


class NextRequestMiddlewareType(Protocol[InstagramType]):  # pragma: no cover
    async def __call__(
        self,
        client: "Client",
        method: "InstagramMethod[InstagramType]",
    ) -> InstagramType:
        pass


class RequestMiddlewareType(Protocol):  # pragma: no cover
    async def __call__(
        self,
        make_request: NextRequestMiddlewareType[InstagramType],
        client: "Client",
        method: "InstagramMethod[InstagramType]",
    ) -> InstagramType:
        pass


class BaseRequestMiddleware(ABC):
    """
    Generic middleware class
    """

    @abstractmethod
    async def __call__(
        self,
        make_request: NextRequestMiddlewareType[InstagramType],
        client: "Client",
        method: "InstagramMethod[InstagramType]",
    ) -> InstagramType:
        """
        Execute middleware

        :param make_request: Wrapped make_request in middlewares chain
        :param client: client for request making
        :param method: Request method (Subclass of :class:`terigrapi.methods.base.InstagramMethod`)

        :return: :class:`terigrapi.methods.InstagramType`
        """
        pass
