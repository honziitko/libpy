"""
Library intrinsics.
"""

_Bool = bool

__all__ = [name for name in globals() if not (name.startswith("__") and name.endswith("__"))]
