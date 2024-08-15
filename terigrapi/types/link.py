from .base import InstagramObject
from .link_context import LinkContext

class Link(InstagramObject):
    text: str
    link_context: LinkContext
    client_context: str
    mutation_token: str