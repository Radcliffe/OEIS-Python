# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A135923

from itertools import islice
def A135923_generator():
    m = [1680, -840, -1380, -240, 641, 393, -209, -10, 0]
    yield m[-1]
    while True:
        for i in range(8):
            m[i+1]+= m[i]
        yield m[-1]
list(islice(A135923_generator(),0,50,1)) # _Chai Wah Wu_, Nov 14 2014

