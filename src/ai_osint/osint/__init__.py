from .dehashed import Dehashed
from .tps import TPS
from .checkleaked import CheckLeaked

def get_all_source_info(
    name: str = None, # dehashed, tps, checkleaked
    phone: str = None, # dehashed, tps
    email: str = None, # dehashed, tps, checkleaked
    username: str = None, # dehashed, checkleaked
    address: str = None, # dehashed, tps
    ip: str = None, # ip2location, dehashed, checkleaked
    domain: str = None, 
    password: str = None, # dehashed, checkleaked
    hashed_password: str = None, # dehashed, checkleaked, md5hashing.net
):
    pass
