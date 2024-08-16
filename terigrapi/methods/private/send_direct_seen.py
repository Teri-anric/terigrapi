from ..base import InstagramMethod, MethodRequestOptions, ClientApiType
from ...types import DirectThread
from ..utils import DefaultDataModel

__all__ = ["SendThreadSeenMethod"]


class SendThreadSeenMethod(InstagramMethod[DirectThread], DefaultDataModel):
    """
    Send seen to thread
    """

    __options__ = MethodRequestOptions(
        returning=dict,
        method="GET",
        endpoint="/v1/direct_v2/threads/{thread_id}/items/{item_id}/seen/",
        api_type=ClientApiType.PRIVATE,
        with_signature=False,
        path_fields={"thread_id", "item_id"},
    )

    thread_id: int
    item_id: int
