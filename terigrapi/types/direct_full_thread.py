
from terigrapi.types.last_seen import LastSeen
from .user import User
from .direct_item import DirectItem

from .base import MutableInstagramObject


class DirectThread(MutableInstagramObject):
    has_older: bool
    has_newer: bool
    pending: bool
    items: list[DirectItem]
    canonical: bool
    thread_id: str
    thread_v2_id: str
    users: list[User]
    viewer_id: int
    muted: bool
    vc_muted: bool
    encoded_server_data_info: str
    admin_user_ids: list[int]
    approval_required_for_new_members: bool
    archived: bool
    thread_has_audio_only_call: bool
    pending_user_ids: list[int]
    last_seen_at: dict[str, LastSeen]
    direct_story: dict[str, Any]
    oldest_cursor: str
    newest_cursor: str
    inviter: User | None = None
    next_cursor: str
    prev_cursor: str
    last_permanent_item: DirectItem | None = None
    icebreakers: list[Icebreaker] | None = None
    snippet: dict[str, Any]
    ig_thread_capabilities: dict[str, Any]
    dismiss_inbox_nudge: bool | None = None
    should_upsell_nudge: bool
    public_chat_metadata: dict[str, Any]
    is_creator_thread: bool
    is_business_thread: bool
    account_warning: str | None = None
    event_thread_metadata: dict[str, Any] | None = None
    group_profile_id: int | None = None
    ctd_outcome_upsell_setting: dict[str, Any] | None = None
    takedown_data: dict[str, Any] | None = None
    is_xac_readonly: bool
    creator_agent_enabled: bool
    read_receipts_disabled: int
    live_location_session_id: str | None = None
    pinned_timestamp: int | None = None
    instamadillo_cutover_metadata: dict[str, Any] | None = None
    boards_call_data: dict[str, Any] | None = None
    is_3p_api_user: bool
    typing_indicator_disabled: int
    locked_status: dict[str, Any] | None = None
    customer_details: dict[str, Any] | None = None
    recurring_prompt_type: int | None = None
    snoozed_messages_metadata: dict[str, Any]
    is_verified_thread: bool
    last_mentioned_item_timestamp_us: int | None = None
    carbon_extra_fields: dict[str, Any] | None = None
    thread_title: str
    thread_label: int
    thread_languages: dict[str, str] | None = None
    is_group: bool
    is_spam: bool
    spam: bool
    shh_mode_enabled: bool
    relevancy_score: int
    relevancy_score_expr: int
    is_translation_enabled: bool
    last_activity_at: int
    last_non_sender_item_at: int
    marked_as_unread: bool
    assigned_admin_id: int
    thread_image: dict[str, Any]
    ad_context_data: dict[str, Any] | None = None
    label_items: list[dict[str, Any]]
    shh_transport_mode: int
    shh_toggler_userid: int | None = None
    messaging_thread_key: int
    policy_violation: dict[str, Any] | None = None
    theme: dict[str, Any]
    thread_context_items: list[dict[str, Any]]
    professional_metadata: dict[str, Any] | None = None
    smart_suggestion: dict[str, Any] | None = None
    system_folder: int
    persistent_menu_icebreakers: dict[str, Any]
    is_xac_thread: bool
    is_fanclub_subscriber_thread: bool
    input_mode: int
    has_reached_message_request_limit: bool | None = None
    last_mentioned_item_id: str | None = None
    thread_type: str
    thread_subtype: int
    btv_enabled_map: dict[str, Any]
    translation_banner_impression_count: int
    read_state: int
    business_thread_folder: int
    is_creator_subscriber_thread: bool
    group_link_joinable_mode: int
    joinable_group_link: str
    folder: int
    e2ee_cutover_status: int
    left_users: list[User]
    is_appointment_booking_enabled: bool
    mentions_muted: bool
    tq_seq_id: int
    named: bool
    is_close_friend_thread: bool
    uq_seq_id: int
    video_call_id: str | None = None
    bc_partnership: bool
    shh_replay_enabled: bool
