import re
from typing import Literal
from pydantic import field_validator, model_validator


from terigrapi.constants import UNSET
from ..base import InstagramMethod, MethodRequestOptions, ClientApiType
from ...types import DirectItem
from ..utils import DefaultDataModel
from ...client.utils import generate_mutation_token
from ...client.session.utils import ig_dumps


__all__ = ["SendDirectMessageMethod"]


class SendDirectMessageMethod(DefaultDataModel, InstagramMethod[DirectItem]):
    """
    Send a direct message to list of users or threads
    """

    __options__ = MethodRequestOptions(
        returning=dict,  # DataExtractorReturn("payload", returning=DirectItem)
        method="POST",
        endpoint="/v1/direct_v2/threads/broadcast/{method}/",
        with_signature=False,
        api_type=ClientApiType.PRIVATE,
        path_fields={"method"},
    )

    method: Literal["text", "link"]

    thread_ids: list[int] | str = UNSET  # ig_dump()
    recipient_users: list[int] | str = UNSET  # ig_dump()

    text: str = UNSET
    # or
    link_text: str = UNSET
    link_urls: str = UNSET  # ig_dumps(re.findall(r"(https?://[^\s]+)", text))

    client_context: str = UNSET  # generate_mutation_token
    mutation_token: str = UNSET  # generate_mutation_token
    offline_threading_id: str = UNSET  # generate_mutation_token

    action: str = "send_item"
    is_shh_mode: str = "0"
    send_attribution: str = "direct_thread"
    nav_chain: str = (
        "1qT:feed_timeline:1,1qT:feed_timeline:2,1qT:feed_timeline:3,7Az:direct_inbox:4,7Az:direct_inbox:5,5rG:direct_thread:7"
    )

    @field_validator("thread_ids", "recipient_users", mode="before")
    @classmethod
    def serialize_list_fields(cls, value):
        if isinstance(value, list):
            return ig_dumps(value)
        return value

    @field_validator("link_urls")
    @classmethod
    def generate_link_urls(cls, value, info):
        if value is UNSET and "link_text" in info.data:
            link_text = info.data["link_text"]
            return ig_dumps(re.findall(r"(https?://[^\s]+)", link_text))
        return value

    @model_validator(mode="before")
    @classmethod
    def generate_tokens(cls, values):
        if (
            values.get("client_context", UNSET) is UNSET
            and values.get("mutation_token", UNSET) is UNSET
            and values.get("offline_threading_id", UNSET) is UNSET
        ):
            token = generate_mutation_token()
            values["client_context"] = token
            values["mutation_token"] = token
            values["offline_threading_id"] = token
        return values
