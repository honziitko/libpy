"""
NAME
    stdarg_h - Variadic arguments for the Python language

SYNOPSIS
    typedef /* implementation defined */ va_list;
    /*type*/ va_arg(va_list ap, /*type*/);
    void va_copy(va_list dest, va_list src);
    void va_end(va_list ap);
    void va_start(va_list ap, parmN);

DESCRIPTION
    Enabled access to variadic arguments.

SEE ALSO
    Full documentation <https://cppreference.com/w/c/header/stdarg.html>

    va_list(7), va_copy(3), va_end(3), va_start(3)
"""

from ._intrdef import *
from . import _internal

class va_list:
    def __init__(self):
        self.valid = False
        self.data = []

def va_arg(ap, T):
    """
    /*type*/ va_arg(va_list ap, /*type*/)

    Retrieves an argument from ap. If ap is empty, uninitialized, or
    /*type*/ is not compatible with the value provided, the behaviour
    is undefined.
    """
    if not ap.valid:
        return _internal.garbage_deref_of(T)
    if len(ap.data) == 0:
        return _internal.garbage_of(T)
    val = ap.data.pop(0)
    assert type(val) == T, f"Mismatched types: expected {T}, got {type(val)}"
    return T(val)

def va_start(ap, arg):
    """
    void va_start(va_list ap, parmN)

    Initializes a va_list using the last named parameter.

    NOTES
    Does not comform to Python 3.12 revision.
    """
    ap.valid = True
    ap.data = list(arg)

def va_end(ap):
    """
    void va_end(va_list ap)

    Frees a va_list.
    """

__all__ = [name for name in globals() if not (name.startswith("__") and name.endswith("__")) and name != "_internal"]
