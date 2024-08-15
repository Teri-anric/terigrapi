from __future__ import annotations
from typing import Literal

from .link import Link
from .expired_placeholder import ExpiredPlaceholder
from .voice_media import VoiceMedia
from .visual_media import VisualMedia
from .xma_media_share import XmaMediaShare
from .base import InstagramObject
from .media import Media
from .action_log import ActionLog
from .reactions import Reactions
from .xma_link import XmaLink


class DirectItem(InstagramObject):
    message_id: str
    item_id: str
    user_id: int
    timestamp: int
    item_type: Literal[
        "text",
        "link",
        "raven_media",
        "raven_media",
        "felix_share",
        "story_share",
        "media",
        "voice_media",
        "placeholder",
        "action_log",
        "animated_media",
        "xma_clip",
        "xma_media_share",
        "xma_link",
        "expired_placeholder",
    ]
    media_share: Media | None = None
    visual_media: VisualMedia = None
    media: Media | None = None
    processed_business_suggestion: bool = False
    text: str | None = None
    action_log: ActionLog | None = None
    xma_link: list[XmaLink] = None
    xma_media_share: list[XmaMediaShare] | None | list = None
    reactions: Reactions | None = None
    client_context: str
    show_forward_attribution: bool
    forward_score: int | None = None
    is_shh_mode: bool
    is_sent_by_viewer: bool = False
    tq_seq_id: int | None = None
    uq_seq_id: int
    otid: str | None = None
    is_ae_dual_send: bool = False
    is_ephemeral_exception: bool = False
    is_disappearing: bool = False
    is_superlative: bool = False
    paid_partnership_info: dict[str, bool]
    # "paid_partnership_info": { "is_paid_partnership": false }
    is_replyable_in_bc: bool = False
    latest_snooze_state: int = 0
    genai_params: dict
    send_attribution: str = None
    xma_clip: list = None
    voice_media: VoiceMedia = None
    replied_to_message: DirectItem = None
    auxiliary_text: str = None
    expired_placeholder: ExpiredPlaceholder = None
    message_item_type: str = None
    link: Link | None = None
