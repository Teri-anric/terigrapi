from typing import Literal

from terigrapi.client.exeptions import ClientNotFoundError, DirectThreadNotFound
from .base import IClient
from terigrapi.methods.private import (
    DirectThreadsMethod,
    DirectPrndingThreadsMethod,
    DirectThreadMethod,
)
from terigrapi.types import Direct, DirectThread

from terigrapi.constants import UNSET


class DirectMixin(IClient):

    async def direct_threads(
        self,
        limit: int = 20,
        selected_filter: Literal["flagged", "unread"] = None,
        thread_message_limit: int = None,
        cursor: str = None,
        **kwargs,
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
                **kwargs,
            )
        )

    async def direct_pending_threads(self, cursor: str = None, **kwargs) -> Direct:
        """
        Get direct message pending threads
        """
        return await self(DirectPrndingThreadsMethod(cursor=cursor, **kwargs))

    async def direct_thread(
        self, thread_id: int, limit: int = 20, cursor: None = None
    ) -> DirectThread:
        try:
            return await self(
                DirectThreadMethod(
                    thread_id=thread_id,
                    limit=limit,
                    cursor=cursor,
                )
            )
        except ClientNotFoundError as e:
            raise DirectThreadNotFound(e, thread_id=thread_id) from e
