from math import ceil
from random import randrange
from gc import get_objects
from . import config

PAGESIZE = 4096 # 4 KB
CHAR_BIT = 8
WORD_SIZE = 8
SIZE_MAX = 1 << CHAR_BIT*WORD_SIZE

def size_t(n):
    return int(n) % SIZE_MAX

def page_end(offset, addr):
    out = ceil(offset / PAGESIZE) * PAGESIZE
    if config.address_enabled:
        out -= addr % PAGESIZE
    return out

def written_garbage_count(dest_size, write_size, addr):
    assert write_size > dest_size
    pag_end = page_end(dest_size, addr)
    return min(pag_end, write_size) - dest_size

def write_garbage(dest, data):
    dest += data

    objs = [o for o in get_objects() if isinstance(o, (list, dict, bytearray))]
    while len(data) > 0:
        i = randrange(len(objs))
        obj = objs[i]
        objs.pop(i)
        written = overwrite_obj(obj, data)
        data = data[written:]

def overwrite_obj(obj, data):
    if isinstance(obj, (list, bytearray)):
        n = min(len(obj), len(data))
        for i in range(n):
            obj[i] = data[i]
        return n
    elif isinstance(obj, dict):
        keys = list(obj.keys())
        n = min(len(keys), len(data) // 2)
        for i in range(n):
            old_key = keys[i]
            new_key = str(data[2*i])
            val = data[2*i + 1]
            del obj[old_key]
            obj[new_key] = val
        if len(data) % 2 != 0:
            new_key = str(data[-1])
            if n == len(keys):
                obj[new_key] = garbage_whatever()
            else:
                old_key = keys[n]
                val = obj[old_key]
                obj[new_key] = val
                del obj[old_key]
        return len(data)


def garbage_whatever():
    typ = randrange(2)
    if typ == 0:
        return garbage_int()
    elif typ == 1:
        return garbage_key()

def garbage_key():
    out = ""
    for i in range(WORD_SIZE):
        out += chr(garbage_uchar())
    return out

def garbage_uchar():
    return randrange(256)

def garbage_int():
    return randrange(1 << SIZE_MAX)

class SegmentationFault(Exception):
    def _init__(self, message="(core dumped)"):
        super().__init__(message)
