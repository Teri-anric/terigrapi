from abc import ABC, abstractmethod
import random
from typing import Any, TYPE_CHECKING

from terigrapi.client.utils import generate_jazoest


if TYPE_CHECKING:
    from .client import Client
    from .session.config import SessionConfig


class BaseDefault(ABC):

    @abstractmethod
    def __call__(self, client: "Client", config: "SessionConfig") -> Any:
        pass


class DefaultFromSettings(BaseDefault):
    __slots__ = ("_parts", "format")

    def __init__(self, parts: str, /, format: str = None) -> None:
        self._parts = tuple(parts.split("."))
        self.format = format

    @property
    def parts(self) -> str:
        return self._parts

    def __str__(self) -> str:
        return f"ClientSetting.{'.'.join(self._parts)}"

    def __repr__(self) -> str:
        return f"<{self}>"

    def __call__(self, client: "Client", config: "SessionConfig") -> Any:
        value = client.setting
        try:
            for part in self.parts:
                value = getattr(value, part)
            if self.format:
                return self.format.format(value)
            return value
        except AttributeError:
            return None


class RandIntStringDefault(BaseDefault):
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def __call__(self, client: "Client", config: "SessionConfig") -> Any:
        return str(random.randint(self.a, self.b))


class JazoestPhoneIdDefault(BaseDefault):
    def __call__(self, client: "Client", config: "SessionConfig") -> Any:
        return generate_jazoest(client.setting.uuids.phone_id)
