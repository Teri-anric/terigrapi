from abc import ABC
from .base import IClient

import base64
import time

from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes

from terigrapi.client.exeptions import ClientError
from terigrapi.methods.public.password_publickeys import GetPasswordPublicKeyMethod


class PasswordMixin(IClient):
    async def password_encrypt(self, password):
        pub = await self(GetPasswordPublicKeyMethod())
        session_key = get_random_bytes(32)

        iv = get_random_bytes(12)
        timestamp = str(int(time.time()))
        decoded_publickey = base64.b64decode(pub.publickey.encode())
        recipient_key = RSA.import_key(decoded_publickey)
        cipher_rsa = PKCS1_v1_5.new(recipient_key)
        rsa_encrypted = cipher_rsa.encrypt(session_key)
        cipher_aes = AES.new(session_key, AES.MODE_GCM, iv)
        cipher_aes.update(timestamp.encode())
        aes_encrypted, tag = cipher_aes.encrypt_and_digest(password.encode("utf8"))
        size_buffer = len(rsa_encrypted).to_bytes(2, byteorder="little")
        payload = base64.b64encode(
            b"".join(
                [
                    b"\x01",
                    pub.publickey_id.to_bytes(1, byteorder="big"),
                    iv,
                    size_buffer,
                    rsa_encrypted,
                    tag,
                    aes_encrypted,
                ]
            )
        )
        # iv = bytearray(12)
        # timestamp = datetime.now().strftime('%s')
        # decoded_publickey = base64.b64decode(publickey.encode())
        # recipient_key = RSA.import_key(decoded_publickey)
        # cipher_rsa = PKCS1_v1_5.new(recipient_key)
        # enc_session_key = cipher_rsa.encrypt(session_key)
        # cipher_aes = AES.new(session_key, AES.MODE_GCM, iv)
        # cipher_aes.update(timestamp.encode())
        # ciphertext, tag = cipher_aes.encrypt_and_digest(password.encode("utf8"))
        # payload = base64.b64encode(b''.join([
        #     b"\x01\x00",
        #     publickeyid.to_bytes(2, byteorder='big'),
        #     iv,
        #     len(enc_session_key).to_bytes(2, byteorder='big'),
        #     enc_session_key,
        #     tag,
        #     ciphertext
        # ]))
        return f"#PWD_INSTAGRAM:4:{timestamp}:{payload.decode()}"
