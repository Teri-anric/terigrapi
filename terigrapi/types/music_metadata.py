from .base import MutableInstagramObject


class MusicMetadata(MutableInstagramObject):
    music_canonical_id: str
    audio_type: str | None
    music_info: dict[str] | None
    original_sound_info: dict[str] | None
