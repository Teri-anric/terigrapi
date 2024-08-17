from pydantic import field_validator
from terigrapi.constants import UNSET
from .send_direct_item import SendDirectItemMethod

__all__ = ["SendStoryDirectMethod"]


class SendStoryDirectMethod(SendDirectItemMethod):
    """
    Share a story to list of users or threads
    """

    story_media_id: str # story_id
    reel_id: str = UNSET # story_pk

    method: str = "story_share"
    send_attribution: str = "reel_feed_timeline"
    containermodule: str = "reel_feed_timeline"
    nav_chain: str = "1qT:feed_timeline:1,ReelViewerFragment:reel_feed_timeline:4,DirectShareSheetFragment:direct_reshare_sheet:5"
    
    
    @field_validator("reel_id")
    @classmethod
    def extract_reel_id(cls, value, info):
        if value is not UNSET:
            return value
        story_media_id = info["story_media_id"]
        reel_id, _ = story_media_id.split('_')
        return reel_id
