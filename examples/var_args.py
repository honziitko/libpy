from libpy.stdarg_h import *

def foo(*args):
    ap = va_list()
    va_start(ap, args)
    while (arg := va_arg(ap, str)) != "HALT":
        print(arg)
    va_end(ap)

foo("Hello", "World!", "HALT")
