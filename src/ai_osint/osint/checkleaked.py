import requests as r
from .env import CHECKLEAKED_API_KEY
from typing import Literal
from typing import Any
import json


class CheckLeaked:

    def __init__(self) -> None:
        self.sess = r.Session()
        self.sess.headers["api-key"] = CHECKLEAKED_API_KEY
        self.sess.headers["Content-Type"] = "application/json"
        self.sess.headers["Accept"] = "application/json"
        self.BASE_URL = "https://api.checkleaked.cc/api"

    def post(
        self,
        entry: str,
        entry_type: Literal["name", "email", "username", "password", "hash", "lastip"],
    ) -> list[dict[str, Any]]:
        response = self.sess.post(
            f"{self.BASE_URL}/experimental", json={"entry": entry, "type": entry_type}
        )
        try:
            return response.json()["results"]
        except KeyError:
            # no results, either rate limited or no data
            return []

    def get_all_info(
        self,
        /,
        *,
        name: str = None,
        email: str = None,
        username: str = None,
        password: str = None,
        hashed_password: str = None,
        ip: str = None,
    ):
        result = []
        if name is not None:
            result += self.by_name(name)
        if email is not None:
            result += self.by_email(email)
        if username is not None:
            result += self.by_username(username)
        if password is not None:
            result += self.by_password(password)
        if hashed_password is not None:
            result += self.by_hashed_password(hashed_password)
            result.append(self.crack_hash(hashed_password))
        if ip is not None:
            result += self.by_ip(ip)
        return result[:256]

    def by_name(self, name: str):
        return self.post(name, "name")

    def by_email(self, email: str):
        return self.post(email, "email")

    def by_username(self, username: str):
        return self.post(username, "username")

    def by_password(self, password: str):
        return self.post(password, "password")

    def by_hashed_password(self, hashed_password: str):
        return self.post(hashed_password, "hash")

    def by_ip(self, ip: str):
        return self.post(ip, "lastip")

    def crack_hash(self, hashed_password: str):
        response = self.sess.post(
            f"{self.BASE_URL}/crack_hash", json={"hash": hashed_password}
        )
        return response.json()


if __name__ == "__main__":
    from .env import TEST_INFO
    import json

    checkleaked = CheckLeaked()
    print(json.dumps(checkleaked.get_all_info(name=TEST_INFO.name), indent=2))
