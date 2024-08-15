from enum import Enum, IntEnum

class ClientApiType(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"
    PUBLIC_GRAPHQL = "public_graphql"
    UNSET = "unset"
    OTHER = "other"


class MediaType(IntEnum):
    voice_media = 11
    visual_media_photo = 1
    visual_media_video = 2
