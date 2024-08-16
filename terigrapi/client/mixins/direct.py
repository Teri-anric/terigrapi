from typing import Literal

from terigrapi.client.exeptions import ClientNotFoundError, DirectThreadNotFound
from .base import IClient
from terigrapi.methods.private import (
    DirectThreadsMethod,
    DirectPrndingThreadsMethod,
    DirectThreadMethod,
    SendDirectMessageMethod,
    SendThreadSeenMethod,
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
        self, thread_id: int, limit: int = 20, cursor: None = None, **kwargs
    ) -> DirectThread:
        try:
            return await self(
                DirectThreadMethod(
                    thread_id=thread_id, limit=limit, cursor=cursor, **kwargs
                )
            )
        except ClientNotFoundError as e:
            raise DirectThreadNotFound(e, thread_id=thread_id) from e

    async def seen_thread_item(self, thread_id: int, item_id: int, **kwargs):
        """
        Send seen to thread
        """
        return await self(
            SendThreadSeenMethod(thread_id=thread_id, item_id=item_id, **kwargs)
        )

    async def send_thread(self, thread_ids: int | list[int], text: str, **kwargs):
        if not isinstance(thread_ids, list):
            thread_ids = [thread_ids]
        return await self.send_direct(text, [], thread_ids, **kwargs)

    async def send_direct(
        self,
        text: str,
        user_ids: list[int] = None,
        thread_ids: list[int] = None,
        check_link: bool = False,
        **kwargs,
    ):
        user_ids = user_ids or []
        user_ids = [int(user_id) for user_id in user_ids]
        thread_ids = thread_ids or []
        thread_ids = [int(thread_id) for thread_id in thread_ids]

        params = {}
        params["method"] = "text"
        params["text"] = text
        if check_link and "http" in text:
            params["method"] = "link"
            params["link_text"] = text
            params.pop("text")

        return await self(
            SendDirectMessageMethod(
                recipient_users=user_ids, thread_ids=thread_ids, **params, **kwargs
            )
        )
