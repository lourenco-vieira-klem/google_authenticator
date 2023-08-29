import hmac
import base64
import struct
import hashlib
import time
import qrcode
import random
import string
import os


class GoogleOauth():
    def generate_qr_code(self, service: str, email: str, secret: str):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L 
        )

        qr.add_data(f"otpauth://totp/{service}:{email}?secret={secret}&issuer={service}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        if not os.path.exists('./generated_qr_code'): 
            os.mkdir('./generated_qr_code')

        img.save("./generated_qr_code/otpauth.png")

    def get_hotp_token(self, secret: str):
        key = base64.b32decode(secret, True)
        msg = struct.pack(">Q", int(time.time())//30)
        h = hmac.new(key, msg, hashlib.sha1).digest()
        o = h[19] & 15
        h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
        return h

    def generate_oauth_secret(self):
        oauth_secret = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(16))
        return oauth_secret
