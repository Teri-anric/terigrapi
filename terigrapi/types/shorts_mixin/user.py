from terigrapi.client.context_controller import ClientContextController

class UserShortsMixin(ClientContextController):
    pk: int
    
    async def send(
        self,
        text: str,
        **kwargs,
    ):
        """Send a text direct message to user"""
        return await self.client.send_direct(text=text, user_ids=[self.pk], **kwargs)

    async def send_media(
        self,
        media_id: str,
        **kwargs,
    ):
        """
        Share a media to user

        :params media_id: it's full media id (can usage media obj prop)
        """
        return await self.client.send_direct_media(
            media_id=media_id, user_ids=[self.pk], **kwargs
        )

    async def send_story(
        self,
        story_media_id: str,
        **kwargs,
    ):
        """
        Share a story to user

        :params story_media_id: it's full story media id (can usage story obj prop)
        """
        return await self.client.send_direct_story(
            story_media_id=story_media_id, user_ids=[self.pk], **kwargs
        )

    async def send_video(
        self,
        upload_id: str,
        **kwargs,
    ):
        """Send a direct video to user"""
        return await self.client.send_direct_video(
            upload_id=upload_id, user_ids=[self.pk], **kwargs
        )

    async def send_photo(
        self,
        upload_id: str,
        **kwargs,
    ):
        """Send a direct photo to user"""
        return await self.client.send_direct_photo(
            upload_id=upload_id, user_ids=[self.pk], **kwargs
        )

