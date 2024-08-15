from typing import Any, Generic, Literal, MutableMapping
import orjson
from pydantic import BaseModel, ConfigDict

from terigrapi.client.exeptions import ClientJSONDecodeError
from terigrapi.constants import InstagramType


class Request(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    method: Literal["GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"]
    url: str
    headers: dict[str, str]
    params: dict[str, Any] | None
    data: dict[str, Any] | None


class Response(BaseModel):
    headers: MutableMapping[str, str]
    cookies: MutableMapping[str, str]
    content: bytes | str
    status_code: int | None

    def json(self):
        try:
            return orjson.loads(self.content)
        except orjson.JSONDecodeError as e:
            raise ClientJSONDecodeError(
                "JSONDecodeError {0!s} ".format(e),
                response=self,
            )
