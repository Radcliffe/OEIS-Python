# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A038103

from sympy.ntheory.digits import digits
from itertools import count, islice, product
def agen(): # generator of terms
    yield 0
    for d in count(1):
        for first in "12":
            for rest in product("012", repeat=d-1):
                s = first + "".join(rest)
                if s in "".join(str(d) for d in digits(int(s), 3)[1:]):
                    yield int(s)
print(list(islice(agen(), 31))) # _Michael S. Branicky_, Jan 08 2022

