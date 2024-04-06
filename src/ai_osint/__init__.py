from .osint import get_all_source_info
from .osint.types import Query
from .ai import generate

BASE_MODEL = "gpt-4-turbo-preview"  # because it has a 128k context window


def ai_osint(
    name: str = None,
    phone: str = None,
    email: str = None,
    username: str = None,
    address: str = None,
    ip: str = None,
    domain: str = None,
    password: str = None,
    hashed_password: str = None,
    debug: bool = False,
    stream: bool = False,
):
    osint_data = get_all_source_info(
        name=name,
        phone=phone,
        email=email,
        username=username,
        address=address,
        ip=ip,
        domain=domain,
        password=password,
        hashed_password=hashed_password,
        debug=debug,
    )
    query = Query(
        name=name,
        phone=phone,
        email=email,
        username=username,
        address=address,
        ip=ip,
        domain=domain,
        password=password,
        hashed_password=hashed_password,
    )

    return generate(BASE_MODEL, query, *osint_data, debug=debug, stream=stream)
