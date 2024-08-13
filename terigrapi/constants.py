from unittest.mock import sentinel
from typing import TYPE_CHECKING, Any, TypeVar


UNSET = sentinel.UNSET
UNSET_TYPE = type(UNSET)


InstagramType = TypeVar("InstagramType", bound=Any)
