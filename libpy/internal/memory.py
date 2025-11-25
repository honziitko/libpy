from math import ceil
from .. import config
from .stddef import PAGESIZE

def page_end(offset, addr):
    out = ceil(offset / PAGESIZE) * PAGESIZE
    if config.address_enabled:
        out -= addr % PAGESIZE
    return out


