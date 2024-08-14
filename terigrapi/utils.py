import hashlib
import time
from uuid import uuid4

def generate_str_uuid():
    return str(uuid4())


def generate_android_device_id() -> str:
        """
        Helper to generate Android Device ID

        Returns
        -------
        str
            A random android device id
        """
        return "android-%s" % hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]


