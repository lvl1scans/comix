from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

import base64
import gzip
import hashlib
import hmac
import json
import os
import requests
import secrets
import sys
import uuid

SCRIPT_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))
DEVICE_ID_PATH = os.path.join(SCRIPT_PATH, "device_id")
TOKENS_PATH = os.path.join(SCRIPT_PATH, "tokens")

if os.path.isfile(DEVICE_ID_PATH):
    with open(DEVICE_ID_PATH, "r") as f:
        DEVICE_ID = f.read()
else:
    with open(DEVICE_ID_PATH, "w") as f:
        DEVICE_ID = secrets.token_hex(16)
        f.write(DEVICE_ID)

def save_tokens(tokens):
    with open(TOKENS_PATH, "w") as f:
        f.write(json.dumps(tokens))
def get_tokens():
    if os.path.isfile(TOKENS_PATH):
        with open(TOKENS_PATH, "r") as f:
            return json.loads(f.read())
    else:
        return None

APP_NAME = "com.amazon.avod.thirdpartyclient"
APP_VERSION = "296016847"
DEVICE_NAME = "walleye/google/Pixel 2"
MANUFACTURER = "Google"
OS_VERSION = "google/walleye/walleye:8.1.0/OPM1.171019.021/4565141:user/release-keys"

def pkcs7_pad(data):
    padsize = 16 - len(data) % 16
    return data + bytes([padsize]) * padsize

def pkcs7_unpad(data):
    offset = data[-1]
    return data[:-offset]

def get_headers(domain):
    return {
        "Accept-Charset": "utf-8",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; Pixel 2 Build/OPM1.171019.021)",
        "x-amzn-identity-auth-domain": f"api.amazon.{domain}",
        "x-amzn-requestid": str(uuid.uuid4()),
    }


def generate_frc(device_id):
    cookies = json.dumps({
        "ApplicationName": APP_NAME,
        "ApplicationVersion": APP_VERSION,
        "DeviceLanguage": "en",
        "DeviceName": DEVICE_NAME,
        "DeviceOSVersion": OS_VERSION,
        "IpAddress": requests.get('https://api.ipify.org').text,
        "ScreenHeightPixels": "1920",
        "ScreenWidthPixels": "1280",
        "TimeZone": "00:00",
    })

    compressed = gzip.compress(cookies.encode())
    
    key = PBKDF2(device_id, b"AES/CBC/PKCS7Padding")
    iv = secrets.token_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pkcs7_pad(compressed))

    hmac_ = hmac.new(PBKDF2(device_id, b"HmacSHA256"), iv + ciphertext, hashlib.sha256).digest()

    return base64.b64encode(b"\0" + hmac_[:8] + iv + ciphertext).decode()


def login(email, password, domain = "com", device_id = DEVICE_ID):
    tokens = get_tokens()
    if tokens and tokens["name"] == email:
        return refresh(tokens)

    body = {
        "auth_data": {
            "use_global_authentication": "true",
            "user_id_password": {
                "password" : password,
                "user_id": email,
            },
        },
        "registration_data": {
            "domain": "DeviceLegacy",
            "device_type": "A43PXU4ZN2AL1",
            "device_serial": device_id,
            "app_name": APP_NAME,
            "app_version": APP_VERSION,
            "device_model": DEVICE_NAME,
            "os_version": OS_VERSION,
            "software_version": "130050002"
        },
        "requested_token_type": ["bearer","mac_dms","store_authentication_cookie","website_cookies"],
        "cookies": {
            "domain": f"amazon.{domain}",
            "website_cookies": []
        },
        "user_context_map": {
            "frc": generate_frc(device_id)
        },
        "device_metadata": {
            "device_os_family": "android",
            "device_type": "A43PXU4ZN2AL1",
            "device_serial": device_id,
            "mac_address": secrets.token_hex(64).upper(),
            "manufacturer": MANUFACTURER,
            "model": DEVICE_NAME,
            "os_version": "30",
            "android_id": "f1c56f6030b048a7",
            "product": DEVICE_NAME
        },
        "requested_extensions": ["device_info","customer_info"]
    }

    response_json = requests.post(f"https://api.amazon.{domain}/auth/register", headers=get_headers(domain), json=body).json()
    try:
        tokens = {
            "name": email,
            "domain": domain,
            "access_token": response_json["response"]["success"]["tokens"]["bearer"]["access_token"],
            "refresh_token": response_json["response"]["success"]["tokens"]["bearer"]["refresh_token"],
            "device_private_key": response_json["response"]["success"]["tokens"]["mac_dms"]["device_private_key"],
            "adp_token": response_json["response"]["success"]["tokens"]["mac_dms"]["adp_token"],
        }
        save_tokens(tokens)
        return tokens
    except:
        print(json.dumps(response_json))
        return None


def refresh(tokens):
    body = {
        "app_name": APP_NAME,
        "app_version": APP_VERSION,
        "source_token_type": "refresh_token",
        "source_token": tokens["refresh_token"],
        "requested_token_type": "access_token"
    }
    
    response_json = requests.post(f"https://api.amazon.com/auth/token", headers=get_headers(tokens["domain"]), json=body).json()
    try:
        tokens["access_token"] = response_json["access_token"]
    except:
        print(json.dumps(response_json))
    return tokens


if __name__ == "__main__":
    arg_count = len(sys.argv)
    if arg_count != 4:
        print("usage: amazon_auth.py <email> <password> <domain>")
        print("domains: com, co.uk, co.jp, de")
        exit()
    
    tokens = login(sys.argv[1], sys.argv[2], sys.argv[3])
    
    if tokens == None:
        print("Could not login!")
    else:
        print(json.dumps(tokens))

