from typing import List, Optional
from pydantic import Field
from ..base import InstagramMethod, MethodRequestOptions, ClientApiType
from ...types import Direct

__all__ = ["DirectPrndingThreadsMethod"]


class DirectPrndingThreadsMethod(InstagramMethod[Direct]):
    """
    Get direct message pending threads
    """

    __options__ = MethodRequestOptions(
        returning=Direct,
        method="GET",
        endpoint="/v1/direct_v2/pending_inbox/",
        api_type=ClientApiType.PRIVATE,
    )

    visual_message_return_type: str = "unseen"
    persistentBadging: str = "true"
    cursor: Optional[str] = None

    # thread_message_limit: int = Field(default=10)
    # limit: int = Field(default=20)
