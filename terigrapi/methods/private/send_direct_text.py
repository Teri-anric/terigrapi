from .send_direct_item import SendDirectItemMethod

__all__ = ["SendTextDirectMethod"]


class SendTextDirectMethod(SendDirectItemMethod):
    """
    Send a text direct message to list of users or threads
    """

    text: str

    method: str = "text"
    nav_chain: str = "1qT:feed_timeline:1,1qT:feed_timeline:2,1qT:feed_timeline:3,7Az:direct_inbox:4,7Az:direct_inbox:5,5rG:direct_thread:7"
    send_attribution: str = "direct_thread"
