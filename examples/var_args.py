#!/usr/bin/env -S PYTHONPATH=. python3
from libpy.stdarg_h import *

def foo(*args):
    ap = va_list()
    va_start(ap, args)
    for i in range(5):
        print(va_arg(ap, str))
    va_end(ap)

def bar(*args):
    ap = va_list()
    va_start(ap, args)
    for i in range(2):
        print(va_arg(ap, int))
    va_end(ap)

foo("Hello", "World!", "HALT")
bar("Hello", "World!")
