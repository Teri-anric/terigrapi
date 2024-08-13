from .image_verison_2 import ImageVersions2
from .media_caption import MediaCaption
from .music_metadata import MusicMetadata
from .base import MutableInstagramObject, InstagramObject
from .user import User
from .short_user import ShortUser

from typing import Any


class SharingFrictionInfo(InstagramObject):
    should_have_sharing_friction: bool
    bloks_app_url: str | None
    sharing_friction_payload: Any | None


class CommentInformTreatment(InstagramObject):
    should_have_inform_treatment: bool
    text: str
    url: str | None
    additional_info: None | Any


class MediaShare(MutableInstagramObject):
    taken_at: int
    pk: int
    id: str
    device_timestamp: int
    media_type: int
    code: str
    client_cache_key: str
    filter_type: int
    is_unified_video: bool
    user: User
    can_viewer_reshare: bool
    caption_is_edited: bool
    like_and_view_counts_disabled: bool
    commerciality_status: str
    is_paid_partnership: bool
    is_visual_reply_commenter_notice_enabled: bool
    comment_likes_enabled: bool
    comment_threading_enabled: bool
    has_more_comments: bool
    max_num_visible_preview_comments: int
    can_view_more_preview_comments: bool
    comment_count: int
    hide_view_all_comment_entrypoint: bool
    image_versions2: ImageVersions2
    original_width: int
    original_height: int
    like_count: int
    has_liked: bool
    likers: list[ShortUser]
    photo_of_you: bool
    is_organic_product_tagging_eligible: bool
    can_see_insights_as_brand: bool
    caption: MediaCaption  # Fix
    can_viewer_save: bool
    organic_tracking_token: str
    has_shared_to_fb: int
    sharing_friction_info: SharingFrictionInfo
    comment_inform_treatment: CommentInformTreatment
    product_type: str
    is_in_profile_grid: bool
    profile_grid_control_enabled: bool
    deleted_reason: int
    integrity_review_decision: str
    music_metadata: MusicMetadata
