"""
NAME
    string_h - A string librabry for Python, as the standard one is lacking.

SYNOPSIS
    void *memset(void *s, int c, size_t n)
    size_t strlen(const char *s)

DESCRIPTION
    A string library for Python. Strings are defined to be a sequence
    of characters terminated by a null byte (\\0), as described by
    ISO/IEC 9899:TC3 section 7.1.1.

NOTES
    These functions, unless stated to the contrary, do not check for
    length. If the string is not null-terminated, or the size
    parameter exceeds the capacity, the behaviour is undefined.

SEE ALSO
    Full documentation <https://en.cppreference.com/w/c/header/string.html>

    memset(3), strlen(3)
"""
from .intrdef import *
from . import internal

def memset(dest, ch, count):
    """
    void *memset(void *dest, int ch, size_t count)

    Fill dest up to count elements with ch and return dest. If count
    exceeds the capacity of dest, assumes the next page does not have
    write permissions.
    """
    count = internal.size_t(count)
    for i in range(min(count, len(dest))):
        dest[i] = ch
    if count > len(dest):
        garbage_size = internal.written_garbage_count(len(dest), count, id(dest))
        garbage = [ch] * garbage_size
        internal.write_garbage(dest, garbage)

        if count >= internal.page_end(len(dest), id(dest)):
            raise internal.SegmentationFault()
    return dest

def strlen(s):
    """
    size_t strlen(const char *s)

    Return the length of s. If no null byte is found, assumes the
    next page does not have read permissions.
    """
    index = s.find('\0')
    if index >= 0:
        return internal.size_t(index)
    until = internal.page_end(len(s), id(s))
    for i in range(len(s), until):
        garbage = internal.garbage_uchar()
        if garbage == 0:
            return internal.size_t(i)
    raise internal.SegmentationFault()

__all__ = [name for name in globals() if not (name.startswith("__") and name.endswith("__")) and name != "internal"]
