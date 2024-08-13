from typing import Any, Coroutine, TYPE_CHECKING

from terigrapi.client.session.middlewares.base import NextRequestMiddlewareType
from terigrapi.methods.base import InstagramMethod, InstagramType
from .base import BaseRequestMiddleware

if TYPE_CHECKING:
    from terigrapi.client.client import Client



class SuppressErrorHandler(BaseRequestMiddleware):
    def __init__(self, *errors: type[Exception]):
        self.error_types = errors
    

    async def __call__(self, make_request: NextRequestMiddlewareType[InstagramType], client: "Client", method: InstagramMethod[InstagramType]) -> Coroutine[Any, Any, InstagramType]:
        try:
            return await make_request(client, method)
        except self.error_types as e:
            return getattr(e, "result", None)


