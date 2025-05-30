# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A368805

from gmpy2 import digits, is_prime
from itertools import count, islice, product
def bgen():
    yield from [2, 3, 5, 7]
    for d in count(2):
        for f in product("2357", repeat=d-1):
            for last in "37":
                yield int("".join(f)+last)
def agen(): yield from (t for t in bgen() if is_prime(t) and set(digits(t, 9)) <= set("2357"))
print(list(islice(agen(), 33))) # _Michael S. Branicky_, Jan 07 2024

