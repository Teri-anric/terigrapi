from __future__ import annotations

from abc import ABC, abstractmethod
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Generator,
    Generic,
    Literal,
)
from pydantic import BaseModel, ConfigDict, Field
from pydantic.functional_validators import model_validator


if TYPE_CHECKING:
    from ..client import Client
    from ..client.session.types import Response
from ..client.context_controller import ClientContextController
from ..enum import ClientApiType
from ..constants import UNSET_TYPE, InstagramType
from ..client.session.middlewares.base import BaseRequestMiddleware
from ..client.default import BaseDefault



class ResultBuild(ABC):
    @abstractmethod
    def __call__(
        self,
        client: "Client",
        method: "InstagramMethod",
        response: "Response"
    ):
        pass


class MethodRequestOptions(BaseModel):
    method: Literal["GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"]
    endpoint: str
    returning: type | ResultBuild | None = None
    api_type: ClientApiType = ClientApiType.UNSET
    with_signature: bool = True
    query_fields: set[str] = Field(default_factory=set)
    path_fields: set[str] = Field(default_factory=set)
    headers: dict[str, str | BaseDefault | None] | BaseDefault = Field(
        default_factory=dict
    )
    middlewares: list[BaseRequestMiddleware] = Field(default_factory=list)
    """field set is remove in POST|PUT|PATCH request and add to query params"""

    class Config:
        arbitrary_types_allowed = True


class InstagramMethod(ClientContextController, BaseModel, Generic[InstagramType], ABC):
    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )

    @model_validator(mode="before")
    @classmethod
    def remove_unset(cls, values: dict[str, Any]) -> dict[str, Any]:
        """
        Remove UNSET before fields validation.
        """
        if not isinstance(values, dict):
            return values
        return {k: v for k, v in values.items() if not isinstance(v, UNSET_TYPE)}

    if TYPE_CHECKING:
        __options__: ClassVar[MethodRequestOptions]
    else:

        @property
        @abstractmethod
        def __options__(self) -> MethodRequestParams:
            pass

    async def emit(self, client: Client) -> InstagramType:
        return await client(self)

    def __await__(self) -> Generator[Any, None, InstagramType]:
        client = self._client
        if not client:
            raise RuntimeError(
                "This method is not mounted to a any client instance, please call it explicilty "
                "with client instance `await client(method)`\n"
                "or mount method to a client instance `method.as_(client)` "
                "and then call it `await method()`"
            )
        return self.emit(client).__await__()
