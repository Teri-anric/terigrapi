from .base import InstagramMethod
from pydantic import Field
from ..client.default import DefaultFromSettings


class DefaultDataModel(InstagramMethod):
    uuid: str = Field(DefaultFromSettings("uuids.uuid"), alias="_uuid")
    device_id: str = DefaultFromSettings("uuids.android_device_id")


class ExtraDataModel(DefaultDataModel):
    phone_id: str = DefaultFromSettings("uuids.phone_id")
    uid: str = Field(DefaultFromSettings("uuids._uid"), alias="_uid")
    guid: str = DefaultFromSettings("uuids.uuid")

