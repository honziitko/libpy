#!/usr/bin/env -S PYTHONPATH=. python3
import libpy
from libpy.stdbool_h import *
from libpy.string_h import *

libpy.set_address_enabled(true)

dest = [1]
memset(dest, 0, -1)
