from unittest.mock import sentinel
from typing import TYPE_CHECKING, Any, TypeVar


UNSET = sentinel.UNSET
UNSET_TYPE = type(UNSET)


InstagramType = TypeVar("InstagramType", bound=Any)



SUPPORTED_CAPABILITIES = [
    {
        "value": "119.0,120.0,121.0,122.0,123.0,124.0,125.0,126.0,127.0,128.0,129.0,130.0,131.0,132.0,133.0,134.0,135.0,136.0,137.0,138.0,139.0,140.0,141.0,142.0",
        "name": "SUPPORTED_SDK_VERSIONS",
    },
    {"value": "14", "name": "FACE_TRACKER_VERSION"},
    {"value": "ETC2_COMPRESSION", "name": "COMPRESSION"},
    {"value": "gyroscope_enabled", "name": "gyroscope"},
]
