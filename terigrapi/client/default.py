from abc import ABC, abstractmethod
import random
from typing import Any, TYPE_CHECKING


from .utils import gen_token, generate_jazoest


import random
import time
from uuid import uuid4
from typing import TYPE_CHECKING

from terigrapi.constants import UNSET

if TYPE_CHECKING:
    from .client import Client
    from .session.base import BaseSession


class BaseDefault(ABC):

    @abstractmethod
    def __call__(self, client: "Client", session: "BaseSession") -> Any:
        pass


class DefaultFromCookie(BaseDefault):
    __slots__ = ("_key", "_default")

    def __init__(self, key: str, default=UNSET) -> None:
        self._key = key
        self._default = default

    def __call__(self, client: "Client", session: "BaseSession") -> Any:
        return session.get_cookies_dict().get(self._key, self._default)


class DefaultCsrftoken(DefaultFromCookie):
    def __init__(self) -> None:
        super().__init__("csrftoken", None)

    def __call__(self, client: "Client", session: "BaseSession") -> Any:
        return super().__call__(client, session) or gen_token(64)


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

    def __call__(self, client: "Client", session: "BaseSession") -> Any:
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

    def __call__(self, client: "Client", session: "BaseSession") -> Any:
        return str(random.randint(self.a, self.b))


class JazoestPhoneIdDefault(BaseDefault):
    def __call__(self, client: "Client", session: "BaseSession") -> Any:
        return generate_jazoest(client.setting.uuids.phone_id)


class DefaultPrivateHeaders(BaseDefault):
    # BLOKS_VERSIONING_ID = hashlib.sha256(
    #     json.dumps(setting.device_settings.model_dump(exclude={"locale"}))
    # ).hexdigest()
    # this param is constant and will change by Instagram app version
    BLOKS_VERSIONING_ID = (
        "ce555e5500576acd8e84a66018f54a05720f2dce29f0bb5a1f97f0c10d6fac48"
    )
    APP_ID = "567067343352427"

    def __call__(self, client: "Client", session: "BaseSession"):
        cl_setting = client.setting
        device_setting = cl_setting.device_settings

        locale = device_setting.locale.replace("-", "_")

        accept_language = ["en-US"]
        if "en-US" != device_setting.locale:
            accept_language = [locale.replace("_", "-"), "en-US"]

        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Authorization": "",
            "X-IG-App-Locale": locale,
            "X-IG-Device-Locale": locale,
            "X-IG-Mapped-Locale": locale,
            "X-Pigeon-Session-Id": f"UFS-{uuid4()}-1",
            "X-Pigeon-Rawclienttime": str(round(time.time(), 3)),
            # "X-IG-Connection-Speed": "-1kbps",
            "X-IG-Bandwidth-Speed-KBPS": str(
                random.randint(2500000, 3000000) / 1000
            ),  # "-1.000"
            "X-IG-Bandwidth-TotalBytes-B": str(
                random.randint(5000000, 90000000)
            ),  # "0"
            "X-IG-Bandwidth-TotalTime-MS": str(random.randint(2000, 9000)),  # "0"
            # "X-IG-EU-DC-ENABLED": "true", # <- type of DC? Eu is euro, but we use US
            # "X-IG-Prefetch-Request": "foreground",  # OLD from instabot
            "X-IG-App-Startup-Country": cl_setting.country.upper(),
            "X-Bloks-Version-Id": self.BLOKS_VERSIONING_ID,
            "X-IG-WWW-Claim": "0",
            # X-IG-WWW-Claim: hmac.AR3zruvyGTlwHvVd2ACpGCWLluOppXX4NAVDV-iYslo9CaDd
            "X-Bloks-Is-Layout-RTL": "false",
            "X-Bloks-Is-Panorama-Enabled": "true",
            "X-IG-Device-ID": cl_setting.uuids.uuid,
            "X-IG-Family-Device-ID": cl_setting.uuids.phone_id,
            "X-IG-Android-ID": cl_setting.uuids.android_device_id,
            "X-IG-Timezone-Offset": str(cl_setting.timezone_offset),
            "X-IG-Connection-Type": "WIFI",
            "X-IG-Capabilities": "3brTvx0=",  # "3brTvwE=" in instabot
            "X-IG-App-ID": self.APP_ID,
            "Priority": "u=3",
            "User-Agent": cl_setting.user_agent,
            "Accept-Language": ", ".join(accept_language),
            "X-MID": cl_setting.mid,  # e.g. X--ijgABABFjLLQ1NTEe0A6JSN7o
            "Accept-Encoding": "zstd, gzip, deflate",
            "X-FB-HTTP-Engine": "Liger",
            "Connection": "keep-alive",
            # "Pragma": "no-cache",
            # "Cache-Control": "no-cache",
            "X-FB-Client-IP": "True",
            "X-FB-Server-Cluster": "True",
            "IG-INTENDED-USER-ID": "0",
            "X-IG-Nav-Chain": (
                "9MV:self_profile:2,ProfileMediaTabFragment:"
                "self_profile:3,9Xf:self_following:4"
            ),
            "X-IG-SALT-IDS": str(random.randint(1061162222, 1061262222)),
        }
        if session.config.domain:
            headers.update(Host=session.config.domain)

        if cl_setting.ig_u_rur:
            headers.update({"IG-U-RUR": '"%s"' % cl_setting.ig_u_rur})
        if cl_setting.ig_www_claim:
            headers.update({"X-IG-WWW-Claim": cl_setting.ig_www_claim})

        if not cl_setting.authorization_data:
            return headers

        user_id = cl_setting.authorization_data.ds_user_id
        if user_id:
            next_year = time.time() + 31536000  # + 1 year in seconds
            headers.update(
                {
                    "Authorization": cl_setting.authorization_data.authorization_header(),
                    "IG-INTENDED-USER-ID": user_id,
                    "IG-U-DS-USER-ID": str(user_id),
                    # Direct:
                    "IG-U-IG-DIRECT-REGION-HINT": (
                        f"LLA,{user_id},{next_year}:"
                        "01f7bae7d8b131877d8e0ae1493252280d72"
                        "f6d0d554447cb1dc9049b6b2c507c08605b7"
                    ),
                    "IG-U-SHBID": (  # ERROR
                        f"12695,{user_id},{next_year}:"
                        "01f778d9c9f7546cf3722578fbf9b85143cd"
                        "6e5132723e5c93f40f55ca0459c8ef8a0d9f"
                    ),
                    "IG-U-SHBTS": (
                        f"{int(time.time())},{user_id},{next_year}:"
                        "01f7ace11925d0388080078d0282b75b8059"
                        "844855da27e23c90a362270fddfb3fae7e28"
                    ),
                    "IG-U-RUR": (
                        f"RVA,{user_id},{next_year}:"
                        "01f7f627f9ae4ce2874b2e04463efdb18434"
                        "0968b1b006fa88cb4cc69a942a04201e544c"
                    ),
                }
            )
        return headers
