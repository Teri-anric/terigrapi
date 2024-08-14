from typing import Any
from .base import MutableInstagramObject



class GrowthFrictionInfo(MutableInstagramObject):
    has_active_interventions: bool
    interventions: dict[str, Any]


class ShortUser(MutableInstagramObject):
    pk: int
    username: str
    full_name: str
    is_private: bool
    profile_pic_url: str
    profile_pic_id: str
    is_verified: bool
    follow_friction_type: int
    growth_friction_info: GrowthFrictionInfo
    account_badges: list[str]
