from .base import MutableInstagramObject
from .fallback import AudioFallback


class Audio(MutableInstagramObject):
    audio_src: str
    duration: int
    audio_src_expiration_timestamp_us: int
    waveform_data: list[float]
    waveform_sampling_frequency_hz: int
    fallback: AudioFallback | None