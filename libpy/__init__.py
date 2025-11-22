from ._intrdef import *
from . import config
from ._core import SegmentationFault

def set_address_enabled(flag):
    assert type(flag) == bool
    config.address_enabled = flag
