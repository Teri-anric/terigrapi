from .send_direct_item import SendDirectItemMethod
from terigrapi.client.default import RandChoicesDefault

__all__ = ["SendVideoDirectMethod"]


class SendVideoDirectMethod(SendDirectItemMethod):
    """
    Send a direct video to list of users or threads
    """

    upload_id: str

    method: str = "configure_video"
    video_result: str = ""
    send_attribution: str = "direct_thread"
    nav_chain: str = RandChoicesDefault(
        [
            "6xQ:direct_media_picker_photos_fragment:1,5rG:direct_thread:2,5ME:direct_quick_camera_fragment:3,5ME:direct_quick_camera_fragment:4,4ju:reel_composer_preview:5,5rG:direct_thread:6,5rG:direct_thread:7,6xQ:direct_media_picker_photos_fragment:8,5rG:direct_thread:9",
            "1qT:feed_timeline:1,7Az:direct_inbox:2,7Az:direct_inbox:3,5rG:direct_thread:4,6xQ:direct_media_picker_photos_fragment:5,5rG:direct_thread:6,5rG:direct_thread:7,6xQ:direct_media_picker_photos_fragment:8,5rG:direct_thread:9",
        ]
    )
