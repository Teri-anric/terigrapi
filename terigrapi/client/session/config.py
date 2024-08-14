from pydantic import BaseModel, ConfigDict, Field
from urllib3.util.url import parse_url

from terigrapi.client.default import BaseDefault
from terigrapi.client.session.middlewares.base import BaseRequestMiddleware
from terigrapi.enum import ClientApiType
from ..default import DefaultPrivateHeaders
from .middlewares.private_errors import PrivateErrorHandler


class SessionConfig(BaseModel):
    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )
    api_url: str = None
    base_headers: dict[str, str | BaseDefault] | BaseDefault = Field(
        default_factory=dict
    )
    cookeis: dict[str, str] = Field(default_factory=dict)
    kwargs: dict | BaseDefault = Field(default_factory=dict)
    middlewares: list[BaseRequestMiddleware] = Field(default_factory=list)

    @property
    def domain(self):
        return parse_url(self.api_url).host


PUBLIC_HEADERS = {
    "Connection": "Keep-Alive",
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "en-US",
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/11.1.2 Safari/605.1.15"
    ),
}

DEFAULT_API_SESSION_CONFIG = {
    ClientApiType.PRIVATE: SessionConfig(
        api_url="https://i.instagram.com/api",
        base_headers=DefaultPrivateHeaders(),
        cookeis={},
        kwargs=dict(verify=False, timeout=45),
        follow_redirects=True,
        middlewares=[PrivateErrorHandler()],
    ),
    ClientApiType.PUBLIC: SessionConfig(
        api_url="https://www.instagram.com/",
        base_headers=PUBLIC_HEADERS,
        cookeis={},
        kwargs=dict(verify=False, timeout=45, follow_redirects=True),
    ),
    ClientApiType.PUBLIC_GRAPHQL: SessionConfig(
        api_url="https://www.instagram.com/graphql/query/",
        base_headers=PUBLIC_HEADERS,
        cookeis={},
        kwargs=dict(verify=False, timeout=45, follow_redirects=True),
    ),
    ClientApiType.UNSET: SessionConfig(
        api_url="", base_headers={}, cookeis={}, kwargs={}
    ),
    ClientApiType.OTHER: SessionConfig(
        api_url="", base_headers={}, cookeis={}, kwargs=dict(verify=False)
    ),
}
