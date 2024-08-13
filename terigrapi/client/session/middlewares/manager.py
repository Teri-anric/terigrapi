from __future__ import annotations

from functools import partial
from typing import Any, Callable, List, Optional, Sequence, Union, cast, overload

from .base import (
    NextRequestMiddlewareType,
    RequestMiddlewareType,
)
from terigrapi.methods.base import InstagramType


class RequestMiddlewareManager(Sequence[RequestMiddlewareType]):
    def __init__(self) -> None:
        self._middlewares: List[RequestMiddlewareType] = []

    def register(
        self,
        middleware: RequestMiddlewareType,
    ) -> RequestMiddlewareType:
        self._middlewares.append(middleware)
        return middleware

    def unregister(self, middleware: RequestMiddlewareType) -> None:
        self._middlewares.remove(middleware)

    def __call__(
        self,
        middleware: Optional[RequestMiddlewareType] = None,
    ) -> Union[
        Callable[[RequestMiddlewareType], RequestMiddlewareType],
        RequestMiddlewareType,
    ]:
        if middleware is None:
            return self.register
        return self.register(middleware)

    @overload
    def __getitem__(self, item: int) -> RequestMiddlewareType:
        pass

    @overload
    def __getitem__(self, item: slice) -> Sequence[RequestMiddlewareType]:
        pass

    def __getitem__(
        self, item: Union[int, slice]
    ) -> Union[RequestMiddlewareType, Sequence[RequestMiddlewareType]]:
        return self._middlewares[item]

    def __len__(self) -> int:
        return len(self._middlewares)

    def wrap_middlewares(
        self,
        callback: NextRequestMiddlewareType[InstagramType],
        **kwargs: Any,
    ) -> NextRequestMiddlewareType[InstagramType]:
        return self._warp_middlewares(self._middlewares, callback, **kwargs)

    @staticmethod
    def _warp_middlewares(middlewares, callback, **kwargs):
        middleware = partial(callback, **kwargs)
        for m in reversed(middlewares):
            middleware = partial(m, middleware)
        return cast(NextRequestMiddlewareType[InstagramType], middleware)
    
