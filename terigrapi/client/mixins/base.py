from typing import TypeVar
from terigrapi.client.session.base import BaseSession
from terigrapi.client.settings import ClientSetting
from terigrapi.enum import ClientApiType
from abc import ABC, abstractmethod

from terigrapi.methods.base import InstagramMethod

T = TypeVar("T")


class IClient(ABC):
    setting: ClientSetting
    sessions: dict[ClientApiType, BaseSession]

    @abstractmethod
    async def __call__(self, method: InstagramMethod[T]) -> T:
        """
        Call API method

        :param method:
        :return:
        """

    pass
