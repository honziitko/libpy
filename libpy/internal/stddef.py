PAGESIZE = 4096 # 4 KB
CHAR_BIT = 8
WORD_SIZE = 8
SIZE_MAX = 1 << CHAR_BIT*WORD_SIZE

def size_t(n):
    return int(n) % SIZE_MAX

class SegmentationFault(Exception):
    def _init__(self, message="(core dumped)"):
        super().__init__(message)
