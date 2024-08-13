from enum import Enum

class ClientApiType(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"
    PUBLIC_GRAPHQL = "public_graphql"
    UNSET = "unset"
    OTHER = "other"

