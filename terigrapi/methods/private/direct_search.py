from ..base import InstagramMethod, MethodRequestOptions, ClientApiType
from ...types import DirectSearch

__all__ = ["DirectSearchMethod"]


class DirectSearchMethod(InstagramMethod[DirectSearch]):
    """
    Search threads by query
    """

    __options__ = MethodRequestOptions(
        returning=DirectSearch,
        method="GET",
        endpoint="/v1/direct_v2/ranked_recipients/",
        api_type=ClientApiType.PRIVATE,
    )
    query: str
    mode: str = "raven"
    show_threads: str = "true"