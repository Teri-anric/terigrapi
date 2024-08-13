from typing import Literal
from .base import IClient
from terigrapi.methods.private import DirectThreadsMethod
from terigrapi.types.direct import Direct

from terigrapi.constants import UNSET


from terigrapi.client.exeptions import TwoFactorRequired, BadCredentials


class DirectMixin(IClient):

    async def get_direct_threads(
        self,
        limit: int = 20,
        selected_filter: Literal["flagged", "unread"] = None,
        thread_message_limit: int = None,
        cursor: str = None,
    ) -> Direct:
        """
        Get direct message threads
        """
        return await self(
            DirectThreadsMethod(
                limit=limit,
                selected_filter=selected_filter or UNSET,
                fetch_reason=("manual_refresh" if selected_filter else UNSET),
                thread_message_limit=thread_message_limit or "10",
                cursor=cursor,
            )
        )
    
