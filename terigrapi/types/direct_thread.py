from .direct_story import DirectStory
from .media import Media
from .theme import Theme
from .base import MutableInstagramObject
from .user import User
from .last_seen import LastSeen
from .direct_item import DirectItem
from .shorts_mixin import ThreadShortsMixin


class DirectThread(MutableInstagramObject, ThreadShortsMixin):
    has_older: bool
    has_newer: bool
    pending: bool
    items: list[DirectItem]
    canonical: bool
    thread_id: str
    thread_v2_id: str
    users: list[User]
    viewer_id: int
    last_activity_at: int
    muted: bool
    vc_muted: bool
    encoded_server_data_info: str
    admin_user_ids: list[int]
    approval_required_for_new_members: bool
    archived: bool
    thread_has_audio_only_call: bool
    pending_user_ids: list[int]
    last_seen_at: dict[str, LastSeen]
    relevancy_score: int
    relevancy_score_expr: int
    oldest_cursor: str
    newest_cursor: str
    inviter: User | None = None
    thread_languages: dict[str, str] | None = None  # paris user_id to language
    last_permanent_item: DirectItem | None = None
    is_xac_thread: bool
    marked_as_unread: bool
    is_creator_subscriber_thread: bool
    group_link_joinable_mode: int
    thread_image: Media | None = None
    shh_replay_enabled: bool
    instamadillo_cutover_metadata: None
    ad_context_data: None
    theme_data: Theme | None = None
    snippet: dict
    is_fanclub_subscriber_thread: bool
    last_mentioned_item_timestamp_us: None
    is_group: bool
    is_close_friend_thread: bool
    mentions_muted: bool
    named: bool
    read_receipts_disabled: int
    btv_enabled_map: dict
    folder: int
    customer_details: None
    joinable_group_link: str
    video_call_id: None
    takedown_data: None
    ctd_outcome_upsell_setting: None
    persistent_menu_icebreakers: dict
    last_mentioned_item_id: None
    recurring_prompt_type: None
    system_folder: int
    input_mode: int
    thread_subtype: int
    icebreakers: None
    theme: dict
    is_xac_readonly: bool
    snoozed_messages_metadata: dict
    shh_mode_enabled: bool
    next_cursor: str
    smart_suggestion: None
    e2ee_cutover_status: int
    left_users: list
    shh_transport_mode: int
    assigned_admin_id: int
    is_business_thread: bool
    event_thread_metadata: None
    live_location_session_id: None
    thread_type: str
    is_spam: bool
    thread_label: int
    professional_metadata: None
    thread_context_items: list
    bc_partnership: bool
    public_chat_metadata: dict
    should_upsell_nudge: bool
    has_reached_message_request_limit: None | bool
    is_3p_api_user: bool
    shh_toggler_userid: None | int
    account_warning: None
    spam: bool
    last_non_sender_item_at: int
    is_verified_thread: bool
    thread_title: str
    policy_violation: None
    is_creator_thread: bool
    read_state: int
    typing_indicator_disabled: int
    business_thread_folder: int
    group_profile_id: None
    translation_banner_impression_count: int
    carbon_extra_fields: None
    prev_cursor: str
    uq_seq_id: int
    tq_seq_id: int | None
    label_items: list
    is_translation_enabled: bool
    messaging_thread_key: int
    pinned_timestamp: None
    dismiss_inbox_nudge: None
    locked_status: None
    ig_thread_capabilities: dict
    is_stale: bool = False
    creator_agent_enabled: bool
    direct_story: DirectStory | None = None
    boards_call_data: None
    is_appointment_booking_enabled: bool
    unpublished_pro_page_id: int | None = None
