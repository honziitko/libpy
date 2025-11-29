from random import randrange
from .stddef import *

def garbage_whatever():
    typ = randrange(3)
    if typ == 0:
        return garbage_int()
    elif typ == 1:
        return garbage_key()
    elif typ == 2:
        return garbage_bool()

def garbage_key():
    out = ""
    for i in range(WORD_SIZE):
        out += chr(garbage_uchar())
    return out

def garbage_uchar():
    return randrange(256)

def garbage_int():
    return randrange(SIZE_MAX)

def garbage_bool():
    return bool(randrange(256))

def garbage_length():
    out = 0
    for i in range(4):
        out += randrange(16)
    return out

def garbage_of(T):
    if T == int:
        return garbage_int()
    elif T == str:
        return garbage_key()
    elif T == bool:
        return garbage_bool()
    elif T == list:
        n = garbage_length()
        return [garbage_whatever() for i in range(n)]
    elif T == bytearray:
        n = garbage_length()
        return bytearray([garbage_uchar() for i in range(n)])
    else:
        assert False, "Unsupported type"

def garbage_deref_of(T):
    if randrange(2) == 0:
        raise SegmentationFault()
    return garbage_of(T)
