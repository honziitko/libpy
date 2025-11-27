from math import ceil
from .. import config
from .stddef import PAGESIZE
from . import enum

def page_end(offset, addr):
    out = ceil(offset / PAGESIZE) * PAGESIZE
    if config.address_enabled:
        out -= addr % PAGESIZE
    return out

TYPCAT_VALUE = enum.new()
TYPCAT_PTR = enum.iota()
TYPCAT_COUNT = enum.iota()

def categorize_type(T):
    if T is int:
        return TYPCAT_VALUE
    elif T in (list, dict, bytearray, str):
        return TYPCAT_PTR
    else:
        raise ValueError("Not implemented")

def bitcast(x, U):
    if type(x) is U:
        return x
    if x is None:
        return U()
    from_cat = categorize_type(type(x))
    to_cat = categorize_type(U)
    if from_cat == TYPCAT_PTR and to_cat == TYPCAT_VALUE:
        assert U is int
        return id(x)
    raise ValueError("Not implemented")
