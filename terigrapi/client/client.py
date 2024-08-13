import time
from typing import Any, TypeVar

from terigrapi.client.exeptions import TwoFactorRequired

from .settings import ClientSetting
from .session import BaseSession, InstagramMethod
from .session import Session
from .session import SessionConfig, DEFAULT_API_SESSION_CONFIG
from terigrapi.enum import ClientApiType
from typing import Coroutine
from .mixins import PasswordMixin


T = TypeVar("T")


class Client(PasswordMixin):

    def __init__(self, setting: ClientSetting = None, session_configs: dict[ClientApiType, SessionConfig] = None) -> None:
        self.setting = setting or ClientSetting()
        # create sessions
        self.sessions = {}
        configs = DEFAULT_API_SESSION_CONFIG | (session_configs or {})
        for api_type, config in configs.items():
            self.sessions[api_type] = Session(self, config)
    
 
    async def __call__(
        self, method: InstagramMethod[T]
    ) -> T:
        """
        Call API method

        :param method:
        :return:
        """
        session = self.sessions.get(method.__options__.api_type, None)
        if session is None:
            raise RuntimeError("Client session not fround.")
        
        return await session(method)
    
    async def sync_launcher(self, login: bool = False):
        from terigrapi.methods.private import SyncLauncherMethod, SyncLoginLauncherMethod

        if login:
            return await self(SyncLoginLauncherMethod())
        return await self(SyncLauncherMethod())


    async def pre_login_flow(self, login: bool = False) -> bool:
        await self.sync_launcher(True)
        return True


    async def login(self,
        username: str,
        password: str,
        verification_code: str = "",
    ) -> bool:
        from terigrapi.methods.private import AccountLoginMethod, TwoFactorAccountLoginMethod

        await self.pre_login_flow(True)
        enc_password = await self.password_encrypt(password)
        try:
            authorization_data = await self(AccountLoginMethod(username=username, enc_password=enc_password))
        except TwoFactorRequired as e:
            if not verification_code.strip():
                raise TwoFactorRequired(
                    f"{e} (you did not provide verification_code for login method)"
                )
            if not isinstance(e.result, dict):
                raise e from e
            two_factor_identifier = e.result.get("two_factor_info", {}).get("two_factor_identifier")
            authorization_data = await self(TwoFactorAccountLoginMethod(
                username=username, 
                verification_code=verification_code, 
                two_factor_identifier=two_factor_identifier
            ))
        else:
            self.setting.authorization_data = authorization_data
            self.setting.last_login = time.time()
            self.setting.username = username
            return True


    async def logout(self, on_tap_app_login: bool = True):
        from terigrapi.methods.private import AccountLogoutMethod

        result = await self(AccountLogoutMethod(
            one_tap_app_login=on_tap_app_login
        ))
        return result["status"] == "ok"

