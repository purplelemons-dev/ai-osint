from .env import DEHASHED_API_KEY, DEHASHED_EMAIL
import requests as r
from base64 import b64encode


class Dehashed:
    def __init__(self) -> None:
        self.sess = r.Session()
        self.sess.headers["Authorization"] = (
            "Basic "
            # b64(email:key)
            + b64encode(f"{DEHASHED_EMAIL}:{DEHASHED_API_KEY}".encode()).decode()
        )
        self.sess.headers["Content-Type"] = "application/json"
        self.sess.headers["Accept"] = "application/json"


    def dehashed(
        self,
        name: str = None,
        phone: str = None,
        email: str = None,
        username: str = None,
        address: str = None,
        ip: str = None,
        domain: str = None,
        password: str = None,
        hashed_password: str = None,
    ):
        pass
