from typing import Any, Dict
from ..constants import UNSET_TYPE

from pydantic import BaseModel, ConfigDict, model_validator

from ..client.context_controller import ClientContextController


class InstagramObject(ClientContextController, BaseModel):
    model_config = ConfigDict(
        use_enum_values=True,
        extra="allow",
        validate_assignment=True,
        frozen=True,
        populate_by_name=True,
        arbitrary_types_allowed=True,
        defer_build=True,
    )

    @model_validator(mode="before")
    @classmethod
    def remove_unset(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """
        Remove UNSET before fields validation.
        """
        if not isinstance(values, dict):
            return values
        return {k: v for k, v in values.items() if not isinstance(v, UNSET_TYPE)}



class MutableInstagramObject(InstagramObject):
    model_config = ConfigDict(
        frozen=False,
    )

