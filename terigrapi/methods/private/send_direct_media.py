from .send_direct_item import SendDirectItemMethod

__all__ = ["SendMediaDirectMethod"]


class SendMediaDirectMethod(SendDirectItemMethod):
    """
    Share a media to list of users or threads
    """

    media_id: str 

    method = "media_share"
    send_attribution: str = "feed_timeline"
    nav_chain: str = "1VL:feed_timeline:1,1VL:feed_timeline:2,1VL:feed_timeline:5,DirectShareSheetFragment:direct_reshare_sheet:6"
    
