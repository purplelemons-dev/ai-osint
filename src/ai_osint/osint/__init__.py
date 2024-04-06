from .dehashed import Dehashed
from .tps import TPS
from .checkleaked import CheckLeaked
from .types import DataSource

dehashed = Dehashed()
tps = TPS()
checkleaked = CheckLeaked()


def get_all_source_info(
    name: str = None,  # dehashed, tps, checkleaked
    phone: str = None,  # dehashed, tps
    email: str = None,  # dehashed, tps, checkleaked
    username: str = None,  # dehashed, checkleaked
    address: str = None,  # dehashed, tps
    ip: str = None,  # ip2location, dehashed, checkleaked
    domain: str = None,  # dehashed
    password: str = None,  # dehashed, checkleaked
    hashed_password: str = None,  # dehashed, checkleaked, md5hashing.net
    debug: bool = False,
) -> list[DataSource]:
    if debug:
        print("Checking CheckLeaked...")
    checkleaked_data = DataSource(
        "CheckLeaked",
        checkleaked.get_all_info(
            name=name,
            email=email,
            username=username,
            ip=ip,
            password=password,
            hashed_password=hashed_password,
        ),
    )

    if debug:
        print("Checking Dehashed...")
    dehashed_data = DataSource(
        "Dehashed",
        dehashed.get_all_info(
            name=name,
            phone=phone,
            email=email,
            username=username,
            address=address,
            domain=domain,
            ip=ip,
            password=password,
            hashed_password=hashed_password,
        ),
    )

    if debug:
        print("Checking TruePeopleSearch...")
    tps_data = DataSource(
        "True-People-Search",
        tps.get_all_info(name=name, phone=phone, email=email, address=address),
    )
    return [checkleaked_data, dehashed_data, tps_data]
