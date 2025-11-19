from libpy.string_h import memset

for i in range(1_000):
    print(i)
    dest = [1]
    memset(dest, 0, -1)
