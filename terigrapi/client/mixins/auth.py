from .base import IClient
from terigrapi.methods.private import AccountLoginMethod, TwoFactorAccountLoginMethod
from terigrapi.methods.private import SyncLauncherMethod, SyncLoginLauncherMethod
from terigrapi.methods.private import (
    GetReelsTrayFeedMethod,
    GetTimelineFeedMethod,
    OneTapAppLoginMethod,
)

import time

from terigrapi.enum import ClientApiType

from terigrapi.client.exeptions import TwoFactorRequired, BadCredentials


class AuthMixin(IClient):
    async def sync_launcher(self, login: bool = False):
        """
        Sync Launcher

        Parameters
        ----------
        login: bool, optional
            Whether to login or not

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        if login:
            return await self(SyncLoginLauncherMethod())
        return await self(SyncLauncherMethod())

    async def pre_login_flow(self, login: bool = False) -> bool:
        """
        Emulation mobile app behavior before login

        Returns
        -------
        bool
            A boolean value
        """
        await self.sync_launcher(True)
        return True

    async def one_tap_app_login(self, user_id: int, nonce: str) -> bool:
        """One tap login emulation

        Parameters
        ----------
        user_id: int
            User ID
        nonce: str
            Login nonce (from Instagram, e.g. in /logout/)

        Returns
        -------
        bool
            A boolean value
        """
        return await self(OneTapAppLoginMethod(user_id=user_id, login_nonce=nonce))

    async def login(
        self,
        username: str,
        password: str,
        verification_code: str = "",
    ) -> bool:
        """
        Login

        Parameters
        ----------
        username: str
            Instagram Username
        password: str
            Instagram Password
        verification_code: str
            2FA verification code

        Returns
        -------
        bool
            A boolean value
        """
        if username is None or password is None:
            raise BadCredentials("Instagram username and password must be provided.")

        await self.pre_login_flow(True)
        enc_password = await self.password_encrypt(password)
        try:
            authorization_data = await self(
                AccountLoginMethod(username=username, enc_password=enc_password)
            )
        except TwoFactorRequired as e:
            if not verification_code.strip():
                raise TwoFactorRequired(
                    f"{e} (you did not provide verification_code for login method)"
                )
            if not isinstance(e.result, dict):
                raise e from e
            two_factor_identifier = e.result.get("two_factor_info", {}).get(
                "two_factor_identifier"
            )
            authorization_data = await self(
                TwoFactorAccountLoginMethod(
                    username=username,
                    verification_code=verification_code,
                    two_factor_identifier=two_factor_identifier,
                )
            )
        else:
            self.setting.authorization_data = authorization_data
            self.setting.last_login = time.time()
            self.setting.username = username
            await self.close()
            return True
    
    async def close(self):
        self.setting.cookies = self.sessions[ClientApiType.PRIVATE].get_cookies_dict()
        for s in self.sessions.values():
            await s.close()
        

    async def logout(self, on_tap_app_login: bool = True):
        from terigrapi.methods.private import AccountLogoutMethod

        result = await self(AccountLogoutMethod(one_tap_app_login=on_tap_app_login))
        return result["status"] == "ok"

    async def get_timeline_feed(self, options: list[str] = ["pull_to_refresh"]) -> dict:
        """
        Get your timeline feed

        Parameters
        ----------
        options: List, optional
            Configurable options

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        if "pull_to_refresh" in options:
            return await self(
                GetTimelineFeedMethod(reason="pull_to_refresh", is_pull_to_refresh="1")
            )
        if "cold_start_fetch" in options:
            return await self(
                GetTimelineFeedMethod(reason="cold_start_fetch", is_pull_to_refresh="0")
            )

    async def get_reels_tray_feed(self, reason: str = "pull_to_refresh") -> dict:
        """
        Get your reels tray feed

        Parameters
        ----------
        reason: str, optional
            Default "pull_to_refresh"

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        return await self(GetReelsTrayFeedMethod(reason=reason))
