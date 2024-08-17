import re

from pydantic import field_validator
from terigrapi.client.session.utils import ig_dumps
from terigrapi.constants import UNSET
from .send_direct_item import SendDirectItemMethod

__all__ = ["SendLinkDirectMethod"]


class SendLinkDirectMethod(SendDirectItemMethod):
    """
    Send a link direct message to list of users or threads
    """

    link_text: str 
    link_urls: str = UNSET  # ig_dumps(re.findall(r"(https?://[^\s]+)", text))
    
    method = "link"
    nav_chain: str = "1qT:feed_timeline:1,1qT:feed_timeline:2,1qT:feed_timeline:3,7Az:direct_inbox:4,7Az:direct_inbox:5,5rG:direct_thread:7"
    send_attribution: str = "direct_thread"

    @field_validator("link_urls")
    @classmethod
    def generate_link_urls(cls, value, info):
        if value is UNSET:
            link_text = info.data["link_text"]
            return ig_dumps(re.findall(r"(https?://[^\s]+)", link_text))
        return value