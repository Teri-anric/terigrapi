from .base import InstagramObject


class PasswordPublicKey(InstagramObject):
    publickey_id: int
    publickey: str
