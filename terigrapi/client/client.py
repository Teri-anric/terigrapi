import time
from typing import Any, TypeVar

from terigrapi.client.exeptions import TwoFactorRequired

from .settings import ClientSetting
from .session import BaseSession, InstagramMethod
from .session import Session
from .session import SessionConfig, DEFAULT_API_SESSION_CONFIG
from terigrapi.enum import ClientApiType
from typing import Coroutine
from .mixins import PasswordMixin, AuthMixin, DirectMixin


T = TypeVar("T")


class Client(PasswordMixin, AuthMixin, DirectMixin):

    def __init__(
        self,
        setting: ClientSetting = None,
        session_configs: dict[ClientApiType, SessionConfig] = None,
    ) -> None:
        self.setting = setting or ClientSetting()
        # create sessions
        self.sessions = {}
        configs = DEFAULT_API_SESSION_CONFIG | (session_configs or {})
        for api_type, config in configs.items():
            self.sessions[api_type] = Session(self, config)

    async def __call__(self, method: InstagramMethod[T]) -> T:
        """
        Call API method

        :param method:
        :return:
        """
        session = self.sessions.get(method.__options__.api_type, None)
        if session is None:
            raise RuntimeError("Client session not fround.")

        return await session(method)
