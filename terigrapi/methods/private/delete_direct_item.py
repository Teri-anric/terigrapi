from pydantic import Field
from terigrapi.client.default import DefaultFromSettings
from terigrapi.client.utils import generate_mutation_token
from ..base import InstagramMethod, MethodRequestOptions, ClientApiType
from ...types import DirectThread

__all__ = ["DeleteThreadItemMethod"]


class DeleteThreadItemMethod(InstagramMethod[DirectThread]):
    """
    Delete a message from thread
    """

    __options__ = MethodRequestOptions(
        returning=dict,
        method="POST",
        endpoint="/v1/direct_v2/threads/{thread_id}/items/{item_id}/delete/",
        api_type=ClientApiType.PRIVATE,
        path_fields={"thread_id", "item_id"},
    )

    thread_id: int
    item_id: int

    uuid: str = Field(DefaultFromSettings("uuids.uuid"), alias="_uuid")
    is_shh_mode: str = "0"
    send_attribution: str = "direct_thread"
    original_message_client_context: str = Field(default_factory=generate_mutation_token) 