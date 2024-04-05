from typing import Any, Literal, TypedDict
import json


class DehashedQuery(TypedDict):
    query: str
    query_type: Literal[
        "name",
        "phone",
        "email",
        "username",
        "address",
        "ip_address",
        "domain",
        "password",
        "hashed_password",
    ]


class DataSource:
    def __init__(self, origin: str, data: dict[str, Any]):
        self.origin: str = origin
        self.data = data


class Query:
    def __init__(
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
        self.name = name
        self.phone = phone
        self.email = email
        self.username = username
        self.address = address
        self.ip = ip
        self.domain = domain
        self.password = password
        self.hashed_password = hashed_password

    def dump(self):
        return json.dumps(
            {
                "name": self.name,
                "phone": self.phone,
                "email": self.email,
                "username": self.username,
                "address": self.address,
                "ip": self.ip,
                "domain": self.domain,
                "password": self.password,
                "hashed_password": self.hashed_password,
            },
            indent=2,
        )
