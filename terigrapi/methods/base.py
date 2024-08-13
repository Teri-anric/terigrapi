from __future__ import annotations

from abc import ABC, abstractmethod
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Dict,
    Generator,
    Generic,
    Optional,
    TypeVar,
    Literal,
    Callable,
    MutableMapping,
)
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field
from pydantic.functional_validators import model_validator


if TYPE_CHECKING:
    from ..client import Client
from ..client.context_controller import ClientContextController
from ..enum import ClientApiType
from ..constants import UNSET_TYPE, InstagramType
from ..client.session.middlewares.base import BaseRequestMiddleware
from ..client.default import BaseDefault


# class Request(BaseModel):
#     model_config = ConfigDict(arbitrary_types_allowed=True)

#     method: str

#     data: Dict[str, Optional[Any]]
#     # files: Optional[Dict[str, InputFile]]


# class Response(BaseModel, Generic[InstagramType]):
#     ok: bool
#     result: Optional[InstagramType] = None
#     description: Optional[str] = None
#     error_code: Optional[int] = None


class ReturnBuild(ABC):
    @abstractmethod
    def __call__(
        self,
        method: "InstagramMethod",
        headers: MutableMapping[str, str] = None,
        cookies: MutableMapping[str, str] = None,
        content: bytes = None,
        error: Exception = None,
    ):
        pass


class ReturnNoneBuild(ReturnBuild):
    def __call__(self, _, __, ___, ____):
        return None


class MethodRequestOptions(BaseModel):
    returning: type | ReturnBuild
    method: Literal["GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"]
    endpoint: str
    api_type: ClientApiType = ClientApiType.UNSET
    with_signature: bool = True
    query_fields: set[str] = Field(default_factory=set)
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
    def remove_unset(cls, values: Dict[str, Any]) -> Dict[str, Any]:
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
