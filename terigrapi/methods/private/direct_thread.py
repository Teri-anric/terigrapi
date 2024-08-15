from typing import List, Optional
from pydantic import Field

from terigrapi.methods.return_builds import DataExtractorReturn
from ..base import InstagramMethod, MethodRequestOptions, ClientApiType
from ...types import DirectThread

__all__ = ["DirectThreadMethod"]


class DirectThreadMethod(InstagramMethod[DirectThread]):
    """
    Get all the information about a Direct Message thread
    """

    __options__ = MethodRequestOptions(
        returning=DataExtractorReturn("thread", returning=DirectThread),
        method="GET",
        endpoint="/v1/direct_v2/threads/{thread_id}/",
        api_type=ClientApiType.PRIVATE,
        path_fields={"thread_id"},
    )

    thread_id: int

    visual_message_return_type: str = "unseen"
    direction: str = "older"
    seq_id: str = "40065"  # 59663
    limit: int = 20
    cursor: Optional[str] = None
