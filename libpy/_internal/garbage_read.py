from random import randrange
from .stddef import *

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


