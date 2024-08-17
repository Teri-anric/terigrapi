from typing import Literal

from terigrapi.client.exeptions import ClientNotFoundError, DirectThreadNotFound
from .base import IClient
from terigrapi.methods.private import (
    DirectThreadsMethod,
    DirectPrndingThreadsMethod,
    DirectThreadMethod,
    SendThreadSeenMethod,
    DeleteThreadItemMethod,
    DirectSearchMethod,
    # ThreadByParticipantsMethod,
    # DirectThreadHideMethod,
    SendTextDirectMethod,
    SendLinkDirectMethod,
    SendMediaDirectMethod,
    SendStoryDirectMethod,
    SendPhotoDirectMethod,
    SendVideoDirectMethod,
    DirectThreadActionMethod,
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

    async def direct_message_delete(self, thread_id: int, item_id: int, **kwargs):
        """
        Delete a message from thread
        """
        return await self(
            DeleteThreadItemMethod(thread_id=thread_id, item_id=item_id, **kwargs)
        )

    async def send_thread(self, thread_ids: int | list[int], text: str, **kwargs):
        if not isinstance(thread_ids, list):
            thread_ids = [thread_ids]
        return await self.send_direct(text, [], thread_ids, **kwargs)

    async def send_direct(
        self,
        text: str,
        user_ids: list[int] = UNSET,
        thread_ids: list[int] = UNSET,
        check_link: bool = False,
        **kwargs,
    ):
        """Send a text direct message to list of users or threads"""
        if check_link and "http" in text:
            return await self(
                SendLinkDirectMethod(
                    link_text=text,
                    recipient_users=user_ids,
                    thread_ids=thread_ids,
                    **kwargs,
                )
            )
        return await self(
            SendTextDirectMethod(
                text=text, recipient_users=user_ids, thread_ids=thread_ids, **kwargs
            )
        )

    async def send_direct_media(
        self,
        media_id: str,
        user_ids: list[int] = UNSET,
        thread_ids: list[int] = UNSET,
        **kwargs,
    ):
        """
        Share a media to list of users

        :params media_id: it's full media id (can usage media obj prop)
        """
        return await self(
            SendMediaDirectMethod(
                media_id=media_id,
                recipient_users=user_ids,
                thread_ids=thread_ids,
                **kwargs,
            )
        )

    async def send_direct_story(
        self,
        story_media_id: str,
        user_ids: list[int] = UNSET,
        thread_ids: list[int] = UNSET,
        **kwargs,
    ):
        """
        Share a story to list of users or threads

        :params story_media_id: it's full story media id (can usage story obj prop)
        """
        return await self(
            SendStoryDirectMethod(
                story_media_id=story_media_id,
                recipient_users=user_ids,
                thread_ids=thread_ids,
                **kwargs,
            )
        )

    async def send_direct_video(
        self,
        upload_id: str,
        user_ids: list[int] = UNSET,
        thread_ids: list[int] = UNSET,
        **kwargs,
    ):
        """Send a direct video to list of users or threads"""
        return await self(
            SendVideoDirectMethod(
                upload_id=upload_id,
                recipient_users=user_ids,
                thread_ids=thread_ids,
                **kwargs,
            )
        )

    async def send_direct_photo(
        self,
        upload_id: str,
        user_ids: list[int] = UNSET,
        thread_ids: list[int] = UNSET,
        **kwargs,
    ):
        """Send a direct photo to list of users or threads"""
        return await self(
            SendPhotoDirectMethod(
                upload_id=upload_id,
                recipient_users=user_ids,
                thread_ids=thread_ids,
                **kwargs,
            )
        )

    async def direct_search(self, query: str, **kwargs):
        """
        Search threads by query

        :param query: Text query, e.g. username
        """
        return await self(DirectSearchMethod(query=query, **kwargs))

    # async def direct_thread_by_participants(self, user_ids: list[int]):
    #     """
    #     Get direct thread by participants

    #     :param user_ids: List of unique identifier of Users id
    #     """
    #     return await self(ThreadByParticipantsMethod(
    #         recipient_users=user_ids
    #     ))

    # '503 Service Unavailable' for url 'https://i.instagram.com/api/v1/direct_v2/threads/5507312766054174/hide/'
    # async def direct_thread_hide(self, thread_id: int):
    #     """
    #     Hide (delete) a thread
    #     When you click delete, Instagram hides a thread

    #     :params thread_id: Id of thread which messages will be read
    #     """
    #     return await self(DirectThreadActionMethod(action="hide", thread_id=thread_id))

    async def direct_thread_mark_unread(self, thread_id: int, **kwargs) -> bool:
        """
        Mark a thread as unread
        """
        return await self(
            DirectThreadActionMethod(
                thread_id=thread_id, action="mark_unread", **kwargs
            )
        )

    async def direct_thread_mute(
        self, thread_id: int, revert: bool = False, **kwargs
    ) -> bool:
        """
        Mute the thread

        :params revert: If muted, whether or not to unmute. Default is False
        """
        return await self(
            DirectThreadActionMethod(
                thread_id=thread_id, action="unmute" if revert else "mute", **kwargs
            )
        )

    async def direct_thread_unmute(self, thread_id: int, **kwargs) -> bool:
        """
        Unmute the thread

        """
        return await self(
            DirectThreadActionMethod(thread_id=thread_id, action="unmute", **kwargs)
        )

    async def direct_thread_mute_video_call(
        self, thread_id: int, revert: bool = False, **kwargs
    ) -> bool:
        """
        Mute video call for the thread

        :params revert: If muted, whether or not to unmute. Default is False
        """
        return await self(
            DirectThreadActionMethod(
                thread_id=thread_id,
                action="unmute_video_call" if revert else "mute_video_call",
                **kwargs,
            )
        )

    async def direct_thread_unmute_video_call(self, thread_id: int, **kwargs) -> bool:
        """
        Unmute video call for the thread
        """
        return await self(
            DirectThreadActionMethod(
                thread_id=thread_id, action="unmute_video_call", **kwargs
            )
        )
