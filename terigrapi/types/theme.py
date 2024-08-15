from __future__ import annotations

from .base import MutableInstagramObject

class IconAsset(MutableInstagramObject):
    fifty: str | None
    seventy_five: str | None
    one_hundred: str | None
    two_hundred: str | None
    icon_images: list[str]

class ThreadBackgroundAsset(MutableInstagramObject):
    four_hundred_eighty: str | None
    seven_hundred_twenty: str | None
    one_thousand_twenty_four: str | None
    two_thousand_forty_eight: str | None
    background_images: list[str]

class AlternativeTheme(MutableInstagramObject):
    theme_id: int
    name: str
    theme_type: int
    alternative_themes: list[AlternativeTheme]
    gradient_colors: list[str]
    is_deprecated: bool
    corner_radius: int
    should_use_diagonal_gradient_for_composer_circle_button: bool
    should_show_incoming_message_bubble_border: bool
    can_display_border_on_visual_message_tombstones: bool
    icon_asset: IconAsset
    secondary_text_color: str
    incoming_message_bubble_color: str
    quoted_incoming_message_bubble_color: str
    thread_background_color: str
    thread_background_asset: ThreadBackgroundAsset
    navigation_bar_color: str
    navigation_bar_title_color: str
    navigation_bar_subtitle_color: str
    navigation_bar_icon_color: str
    solid_composer_background_color: str
    blurred_composer_background_color: str
    composer_secondary_button_color: str
    composer_placeholder_text_color: str = None
    reaction_pill_color: str
    emphasized_action_color: str
    emphasis_colors: list[str]
    solid_separator_color: str
    shh_mode_interleaved_background_color: str
    blurred_composer_opaque_background_color: str
    app_color_mode: str
    fallback_color: str
    inbound_message_text_color: str = None
    outbound_message_text_color: str = None
    composer_send_button_colors: list[str]
    composer_input_background_color: str
    composer_circle_button_colors: list[str]

class Theme(MutableInstagramObject):
    theme_id: int
    name: str
    theme_type: int
    alternative_themes: list[AlternativeTheme]
    gradient_colors: list[str]
    is_deprecated: bool
    corner_radius: int
    should_use_diagonal_gradient_for_composer_circle_button: bool
    should_show_incoming_message_bubble_border: bool
    can_display_border_on_visual_message_tombstones: bool
    icon_asset: IconAsset
    secondary_text_color: str
    incoming_message_bubble_color: str
    quoted_incoming_message_bubble_color: str
    thread_background_color: str
    thread_background_asset: ThreadBackgroundAsset
    navigation_bar_color: str
    navigation_bar_title_color: str
    navigation_bar_subtitle_color: str
    navigation_bar_icon_color: str
    solid_composer_background_color: str
    blurred_composer_background_color: str
    composer_secondary_button_color: str
    composer_placeholder_text_color: str = None
    reaction_pill_color: str
    emphasized_action_color: str
    emphasis_colors: list[str]
    solid_separator_color: str
    shh_mode_interleaved_background_color: str
    blurred_composer_opaque_background_color: str
    app_color_mode: str
    fallback_color: str
    inbound_message_text_color: str
    outbound_message_text_color: str
    composer_send_button_colors: list[str]
    composer_input_background_color: str
    composer_circle_button_colors: list[str]
