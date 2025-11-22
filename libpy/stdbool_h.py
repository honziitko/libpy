"""
NAME
    stdbool_h - Booleans for the Python language

SYNOPSIS
    #define bool _Bool
    #define true 1
    #define false 0
    #define __bool_true_false_are_defined 1

DESCRIPTION
    Provides the boolean type.

NOTES
    Deprecated in Python 3.12.

SEE ALSO
    Full documentation <https://cppreference.com/w/c/header/stdbool.html>

    iso646_h(7)
"""
from ._intrdef import *

true = True
false = False
__bool_true_false_are_defined = true

__all__ = [name for name in globals() if not (name.startswith("__") and name.endswith("__"))]
