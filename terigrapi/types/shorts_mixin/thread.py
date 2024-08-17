from typing import TYPE_CHECKING
from terigrapi.client.context_controller import ClientContextController
if TYPE_CHECKING:
    from ..direct_item import DirectItem

class ThreadShortsMixin(ClientContextController):
    thread_v2_id: int
    items: "list[DirectItem] | None"
    
    async def seen(self, **kwargs):
        """
        Send seen last item of thread
        """
        if not self.items:
            raise ValueError("Can't seen thread, thread not items.")

        return await self.client.seen_thread_item(
            thread_id=self.thread_v2_id, item_id=self.items[0].item_id, **kwargs
        )

    async def answer(self, text: str, **kwargs):
        """
        Send text message to thread
        """
        return await self.client.send_direct(
            text=text, thread_ids=[self.thread_v2_id], **kwargs
        )

    async def answer_media(
        self,
        media_id: str,
        **kwargs,
    ):
        """
        Share a media to user

        :params media_id: it's full media id (can usage media obj prop)
        """
        return await self.client.send_direct_media(
            media_id=media_id, thread_ids=[self.thread_v2_id], **kwargs
        )

    async def answer_story(
        self,
        story_media_id: str,
        **kwargs,
    ):
        """
        Share a story to thread

        :params story_media_id: it's full story media id (can usage story obj prop)
        """
        return await self.client.send_direct_story(
            story_media_id=story_media_id, thread_ids=[self.thread_v2_id], **kwargs
        )

    async def answer_video(
        self,
        upload_id: str,
        **kwargs,
    ):
        """
        Send a direct video to thread

        :params upload_id: client_upload()
        """
        return await self.client.send_direct_video(
            upload_id=upload_id, thread_ids=[self.thread_v2_id], **kwargs
        )

    async def answer_photo(
        self,
        upload_id: str,
        **kwargs,
    ):
        """
        Send a direct photo to thread

        """
        return await self.client.send_direct_photo(
            upload_id=upload_id, thread_ids=[self.thread_v2_id], **kwargs
        )

    async def mute(self, revert: bool = False, **kwargs) -> bool:
        """
        Mute the thread

        :params revert: If muted, whether or not to unmute. Default is False
        """
        return await self.client.direct_thread_mute(
            self.thread_v2_id, revert=revert, **kwargs
        )

    async def unmute(self, **kwargs) -> bool:
        """
        Unmute the thread

        """
        return await self.client.direct_thread_unmute(self.thread_v2_id, **kwargs)

    async def mute_video_call(self, revert: bool = False, **kwargs) -> bool:
        """
        Mute video call for the thread

        :params revert: If muted, whether or not to unmute. Default is False
        """
        return await self.client.direct_thread_mute_video_call(
            self.thread_v2_id, revert=revert, **kwargs
        )

    async def unmute_video_call(self, **kwargs) -> bool:
        """
        Unmute video call for the thread
        """
        return await self.client.direct_thread_unmute_video_call(
            self.thread_v2_id, **kwargs
        )
