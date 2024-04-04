import requests as r
from .env import CHECKLEAKED_API_KEY


class CheckLeaked:

    def __init__(self) -> None:
        self.sess = r.Session()
        self.sess.headers["api-key"] = CHECKLEAKED_API_KEY

    def get_all_info(
        self,
        name: str = None,
        email: str = None,
        username: str = None,
        password: str = None,
        hashed_password: str = None,
        ip: str = None,
    ):
        pass

    def by_name(self, name: str):
        pass

    def by_email(self, email: str):
        pass

    def by_username(self, username: str):
        pass

    def by_password(self, password: str):
        pass

    def by_hashed_password(self, hashed_password: str):
        pass

    def by_ip(self, ip: str):
        pass

    def crack_hash(self, hash: str):
        pass
