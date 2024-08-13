from typing import List, Optional
from pydantic import Field
from ..base import InstagramMethod, MethodRequestOptions, ClientApiType
from ...types import Direct

__all__ = ["DirectThreadsMethod"]

class DirectThreadsMethod(InstagramMethod[Direct]):
    """
    Get direct message threads
    """

    __options__ = MethodRequestOptions(
        returning=Direct,
        method="GET",
        endpoint="/v1/direct_v2/inbox/",
        api_type=ClientApiType.PRIVATE,
    )

    visual_message_return_type: str = "unseen"
    thread_message_limit: int = Field(default=10)
    persistentBadging: str = "true"
    limit: int = Field(default=20)
    selected_filter: Optional[str] = None
    fetch_reason: Optional[str] = None
    cursor: Optional[str] = None
