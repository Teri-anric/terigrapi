from types import TracebackType
from typing import Any, TypeVar

from .context_controller import ClientContextController


from .settings import ClientSetting
from .session import (
    BaseSession,
    HttpxSession,
    SessionConfig,
    DEFAULT_API_SESSION_CONFIG,
)
from terigrapi.methods import InstagramMethod
from terigrapi.enum import ClientApiType
from .mixins import PasswordMixin, AuthMixin, DirectMixin


T = TypeVar("T")


class Client(PasswordMixin, AuthMixin, DirectMixin):

    def __init__(
        self,
        setting: ClientSetting = None,
        *,
        sessions: dict[ClientApiType, BaseSession] = None,
        session_configs: dict[ClientApiType, SessionConfig] = None,
        session_default_cls: type[BaseSession] = HttpxSession,
    ) -> None:
        self.setting = setting or ClientSetting()
        # create sessions
        session_configs = DEFAULT_API_SESSION_CONFIG | (session_configs or {})
        self.sessions = sessions or {}
        for api_type, config in session_configs.items():
            if api_type in self.sessions:
                continue
            self.sessions[api_type] = session_default_cls(config)

    async def __call__(self, method: InstagramMethod[T]) -> T:
        """
        Call API method

        :param method:
        :return:
        """
        session = self.sessions.get(method.__options__.api_type, None)
        if session is None:
            raise RuntimeError("Client session not fround.")
        
        result = await session(self, method)
        # bind by self(Client)
        if isinstance(result, ClientContextController):
            result.as_(client=self)
        return result
        

    
    async def __aenter__(self) -> "Client":
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] = None,
        exc_value: BaseException = None,
        traceback: TracebackType = None,
    ) -> None:
        await self.close()