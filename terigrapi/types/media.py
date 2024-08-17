from terigrapi.enum import MediaType
from .audio import Audio
from .image_verison_2 import ImageVersions2
from .url_info import VideoUrlInfo
from .media_caption import MediaCaption
from .music_metadata import MusicMetadata
from .base import MutableInstagramObject, InstagramObject
from .user import User
from .short_user import ShortUser

from typing import Any, Literal


class SharingFrictionInfo(InstagramObject):
    should_have_sharing_friction: bool
    bloks_app_url: str | None
    sharing_friction_payload: Any | None


class CommentInformTreatment(InstagramObject):
    should_have_inform_treatment: bool
    text: str
    url: str | None
    additional_info: None | Any


class Media(MutableInstagramObject):
    taken_at: int = None
    pk: int = None
    id: int 
    device_timestamp: int = None
    media_id: int = None
    media_type: MediaType
    product_type: Literal["direct_audio"] = None
    code: str = None
    client_cache_key: str = None
    filter_type: int = None
    is_unified_video: bool = None
    user: User = None
    can_viewer_reshare: bool = False
    caption_is_edited: bool = False
    like_and_view_counts_disabled: bool = False
    commerciality_status: str = None
    is_paid_partnership: bool = False
    is_visual_reply_commenter_notice_enabled: bool = False
    comment_likes_enabled: bool = False
    comment_threading_enabled: bool = False
    has_more_comments: bool = False
    max_num_visible_preview_comments: int = None
    can_view_more_preview_comments: bool = False
    comment_count: int = None
    hide_view_all_comment_entrypoint: bool = False
    image_versions2: ImageVersions2 = None # in voice is None
    original_width: int = None # in voice is None
    original_height: int = None # in voice is None
    like_count: int = None
    has_liked: bool = None
    likers: list[ShortUser] = None
    photo_of_you: bool = False
    is_organic_product_tagging_eligible: bool = False
    can_see_insights_as_brand: bool = False
    caption: MediaCaption = None
    can_viewer_save: bool = False
    organic_tracking_token: str = None
    has_shared_to_fb: int = None
    sharing_friction_info: SharingFrictionInfo = None
    comment_inform_treatment: CommentInformTreatment = None
    is_in_profile_grid: bool = False
    profile_grid_control_enabled: bool = False
    deleted_reason: int = None
    integrity_review_decision: str = None
    music_metadata: MusicMetadata = None
    video_versions: list[VideoUrlInfo] = None
    video_duration: int = None
    expiring_media_action_summary: None = None
    create_mode_attribution: None = None
    creative_config: None = None
    audio: Audio = None

    @property
    def full_media_id(self):
        media_id = str(self.pk or self.id)
        if "_" in media_id:
            return media_id
        if not self.user:
            raise ValueError("Can't build media_id, media obj has not user")
        return f"{media_id}_{self.user.pk_id}"
        