import libpy
from libpy.stdbool_h import *
from libpy.string_h import *

libpy.set_address_enabled(true)

for i in range(1_000):
    print(i)
    dest = [1]
    memset(dest, 0, -1)
