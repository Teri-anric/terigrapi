from typing import Optional
from uuid import uuid4
import base64
from pydantic import BaseModel, AnyUrl, Field, model_validator, root_validator
from .utils import gen_token
from terigrapi.utils import generate_android_device_id, generate_str_uuid



class ClientUUIDs(BaseModel):
    phone_id: str = Field(default_factory=generate_str_uuid)
    uuid: str = Field(default_factory=generate_str_uuid)
    client_session_id: str = Field(default_factory=generate_str_uuid)
    advertising_id: str = Field(default_factory=generate_str_uuid)
    android_device_id: str = Field(default_factory=generate_android_device_id)
    request_id: str = Field(default_factory=generate_str_uuid)
    tray_session_id: str = Field(default_factory=generate_str_uuid)


class ClientAuthorization(BaseModel):
    ds_user_id: str
    sessionid: str 
    should_use_header_over_cookies: bool = None

    def authorization_header(self):
        b64part = base64.b64encode(self.model_dump_json(exclude='should_use_header_over_cookies').encode()).decode()
        return f"Bearer IGT:2:{b64part}"
    
    @classmethod
    def from_authorization_header(cls, authorization: str) -> Optional["ClientAuthorization"]:
        try:
            b64part = authorization.rsplit(":", 1)[-1]
            if b64part:
                return cls.model_validate_json(base64.b64decode(b64part))
        except:
            pass


class ClientDevice(BaseModel):
    app_version: str = "289.0.0.25.49"
    android_version: int = 29
    android_release: str = "10"
    dpi: str = "480dpi"
    resolution: str = "1080x2031"
    manufacturer: str = "HUAWEI"
    device: str = "HWEML"
    model: str = "EML-L29"
    cpu: str = "kirin970"
    version_code: str = "488780865"
    locale: str = "uk_UA"

    def to_user_agent(self):
        return (
            f"Instagram {self.app_version} "
            f"Android ({self.android_version}/{self.android_release}; "
            f"{self.dpi}; {self.resolution}; {self.manufacturer}; "
            f"{self.model}; {self.device}; {self.cpu}; "
            f"{self.locale}; {self.version_code})"
        )


class ClientSetting(BaseModel):
    username: str | None = None
    last_login: float = None

    uuids: ClientUUIDs = Field(..., default_factory=ClientUUIDs)
    authorization_data: ClientAuthorization = None # decoded authorization header
    device_settings: ClientDevice = Field(..., default_factory=ClientDevice)
    cookies: dict[str, str] = Field(..., default_factory=dict)

    mid: str | None = None
    ig_u_rur: str | None = None
    ig_www_claim: str = "0"
    user_agent: str = None
    country: str = "UA"
    country_code: int = 1 # Phone code, default USA
    timezone_offset: int = 10800 # Київ, GMT+3 in seconds

    @model_validator(mode="after")
    def post_init_logic(cls, values):
        # If `mid` is not provided, get it from cookies
        if values.mid is None:
            values.mid = values.cookies.get('mid')
        
        # If `user_agent` is not provided, generate it using device_settings
        if values.user_agent is None:
            values.user_agent = values.device_settings.to_user_agent()

        return values

    @property
    def token(self):
        return self.cookies.get("F", gen_token(64))
