from typing import List, Optional
from pydantic import Field, field_validator

from terigrapi.client.session.utils import ig_dumps
from terigrapi.methods.return_builds import DataExtractorReturn
from ..base import InstagramMethod, MethodRequestOptions, ClientApiType
from ...types import DirectSearch

__all__ = ["ThreadByParticipantsMethod"]

# can't test unknown error
# {"action":"item_ack","status_code":"400","message":"None","payload":{"client_context":null,"message":"None"},"status":"fail"}
class ThreadByParticipantsMethod(InstagramMethod[DirectSearch]):
    """
    Get direct thread by participants

    """

    __options__ = MethodRequestOptions(
        returning=dict,
        method="GET",
        endpoint="/v1/direct_v2/threads/get_by_participants/",
        api_type=ClientApiType.PRIVATE,
    )
    recipient_users: str | list[int]
    seq_id: int = 2580572
    limit: int = 20

    @field_validator("recipient_users", mode="before")
    @classmethod
    def serialize_list_fields(cls, value):
        if isinstance(value, list):
            return ig_dumps(value)
        return value