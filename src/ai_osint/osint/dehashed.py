from .env import DEHASHED_API_KEY, DEHASHED_EMAIL
import requests as r
from base64 import b64encode
from .types import DehashedQuery


class Dehashed:
    def __init__(self) -> None:
        self.sess = r.Session()
        self.sess.headers["Authorization"] = (
            # `Authorization: Basic b64(email:key)`
            "Basic "
            + b64encode(f"{DEHASHED_EMAIL}:{DEHASHED_API_KEY}".encode()).decode()
        )
        self.sess.headers["Content-Type"] = "application/json"
        self.sess.headers["Accept"] = "application/json"

    def get(self, queries: list[DehashedQuery]) -> list[dict[str, str]]:
        query_string = ""
        for query in queries:
            query_string += f"{query['query_type']}:{query['query']}&"
        response = self.sess.get(
            f"https://api.dehashed.com/search?query={query_string}page=1&size=2048"
        ).json()
        return response["entries"]

    def get_all_info(
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
        query_list = []
        individual_queries = []
        if name is not None:
            query_list.append({"query": name, "query_type": "name"})
            individual_queries.append(self.get([{"query": name, "query_type": "name"}]))
        if phone is not None:
            query_list.append({"query": phone, "query_type": "phone"})
            individual_queries.append(
                self.get([{"query": phone, "query_type": "phone"}])
            )
        if email is not None:
            query_list.append({"query": email, "query_type": "email"})
            individual_queries.append(
                self.get([{"query": email, "query_type": "email"}])
            )
        if username is not None:
            query_list.append({"query": username, "query_type": "username"})
            individual_queries.append(
                self.get([{"query": username, "query_type": "username"}])
            )
        if address is not None:
            query_list.append({"query": address, "query_type": "address"})
            individual_queries.append(
                self.get([{"query": address, "query_type": "address"}])
            )
        if ip is not None:
            query_list.append({"query": ip, "query_type": "ip_address"})
            individual_queries.append(
                self.get([{"query": ip, "query_type": "ip_address"}])
            )
        if domain is not None:
            query_list.append({"query": domain, "query_type": "domain"})
            individual_queries.append(
                self.get([{"query": domain, "query_type": "domain"}])
            )
        if password is not None:
            query_list.append({"query": password, "query_type": "password"})
            individual_queries.append(
                self.get([{"query": password, "query_type": "password"}])
            )
        if hashed_password is not None:
            query_list.append(
                {"query": hashed_password, "query_type": "hashed_password"}
            )
            individual_queries.append(
                self.get([{"query": hashed_password, "query_type": "hashed_password"}])
            )
        return self.get(query_list) + individual_queries


if __name__ == "__main__":
    from .env import TEST_INFO

    d = Dehashed()
    print(d.get_all_info(email=TEST_INFO.email))
