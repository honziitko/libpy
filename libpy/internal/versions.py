C89 = (1, 0)
C90 = C89
C95 = (1, 2)
C99 = (2, 2)
C11 = (3, 2)
C17 = (3, 7)
C23 = (3, 12)

def _get():
    from sys import version_info
    return version_info[:2]

def check(low, high, assumed = None):
    current = assumed or _get()
    if low is not None and current < low:
        return False
    if high is not None and current >= high:
        return False
    return True
