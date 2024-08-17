import re
from typing import Literal
from pydantic import field_validator, model_validator


from terigrapi.constants import UNSET
from ..base import InstagramMethod, MethodRequestOptions, ClientApiType
from ...types import DirectResponse
from ..utils import DefaultDataModel
from ...client.utils import generate_mutation_token
from ...client.session.utils import ig_dumps


__all__ = ["SendDirectItemMethod"]


class SendDirectItemMethod(InstagramMethod[DirectResponse], DefaultDataModel):
    """
    Send a direct message to list of users or threads
    """

    __options__ = MethodRequestOptions(
        returning=DirectResponse,
        method="POST",
        endpoint="/v1/direct_v2/threads/broadcast/{method}/",
        with_signature=False,
        api_type=ClientApiType.PRIVATE,
        path_fields={"method"},
    )

    method: Literal["text", "link", "media_share", "story_share", "configure_video", "configure_photo"]

    
    thread_ids: list[int] | str = UNSET  # ig_dump()
    recipient_users: list[int] | str = UNSET  # ig_dump()

    client_context: str = UNSET  # generate_mutation_token
    mutation_token: str = UNSET  # generate_mutation_token
    offline_threading_id: str = UNSET  # generate_mutation_token

    action: str = "send_item"
    is_shh_mode: str = "0"
    
    @field_validator("thread_ids", "recipient_users", mode="before")
    @classmethod
    def serialize_list_fields(cls, value):
        if isinstance(value, list):
            return ig_dumps(value)
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
