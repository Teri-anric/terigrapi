from .base import MutableInstagramObject
from .url_info import ImageUrlInfo

class XmaMediaShare(MutableInstagramObject):
    xma_template_type: str | None
    xma_layout_type: int
    preview_url: str
    preview_url_mime_type: str | None
    preview_width: int
    preview_height: int
    title_text: str
    max_title_num_of_lines: int
    max_subtitle_num_of_lines: int
    subtitle_text: str | None
    subtitle_decoration_type: str | None
    default_cta_type: str | None
    default_cta_title: str | None
    header_icon_url: str | None
    header_icon_mime_type: str | None
    header_icon_width: int | None
    header_icon_height: int | None
    header_title_text: str | None
    header_subtitle_text: str | None
    header_cta_type: str | None
    header_cta_title: str | None
    header_icon_layout_type: int
    header_icons_count: int | None
    caption_body_text: str | None
    group_name: str | None
    preview_media_fbid: int
    target_url: str
    ig_template_type: str | None
    playable_width: int
    playable_height: int
    playable_url: str | None
    video_codec: str | None
    video_dash_manifest: str | None
    playable_url_mime_type: str | None
    preview_url_info: ImageUrlInfo | None
    header_icon_url_info: ImageUrlInfo | None
    header_icons_url_info: list[ImageUrlInfo] | None
    playable_url_info: dict | None
    favicon_url_info: dict | None
    favicon_style: str | None
    preview_image_decoration_type: str | None
    cta_buttons: list[dict] | None
    is_quoted: bool | None
    is_borderless: bool | None
    is_sharable: bool
    verified_type: int
    accessibility_summary_text: str | None
    accessibility_summary_hint: str | None
    collapsible_id: str | None
    countdown_timestamp_ms: int | None
    presence_source: str | None
    should_respect_server_preview_size: bool | None
    accessory_preview_url_info: dict | None
    accessory_playable_url_info: dict | None
    playable_audio_url: str | None
    preview_icon_info: dict | None
    quoted_attribution_text: str | None
    quoted_caption_body_text: str | None
    quoted_title_text: str | None
    quoted_favicon_url_info: dict | None
    quoted_author_verified_type: int | None
    save_icon_state: int
    should_refresh: bool
    preview_extra_urls_info: list[dict] | None
    preview_layout_type: int
    serialized_content_ref: str | None

