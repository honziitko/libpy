import libpy
from libpy.string_h import *

libpy.set_address_enabled(True)

for i in range(1_000):
    print(i)
    dest = [1]
    memset(dest, 0, -1)
