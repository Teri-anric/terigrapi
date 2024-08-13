from pydantic import Field
from ..base import InstagramMethod, MethodRequestOptions, ClientApiType, ReturnNoneBuild
from ...client.default import DefaultFromSettings
from ...client.settings import ClientSetting


class SyncLoginLauncherMethod(InstagramMethod[dict]):
    """
    Sync Launcher
    """
    __options__ = MethodRequestOptions(
        returning=dict,
        method="POST",
        endpoint="/v1/launcher/sync/",
        api_type=ClientApiType.PRIVATE,
    )

    id: str = DefaultFromSettings("uuids.uuid")
    server_config_retrieval: str = "1"


class SyncLauncherMethod(SyncLoginLauncherMethod):
    """
    Sync Launcher
    """
    uid: str = Field(DefaultFromSettings("authorization_data.ds_user_id"), alias="_uid")
    uuid: str = Field(DefaultFromSettings("uuids.uuid"), alias="_uuid")
    csrftoken: str = Field(DefaultFromSettings("token"), alias="_csrftoken")


