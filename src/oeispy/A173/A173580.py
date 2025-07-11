# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A173580

from sympy import isprime
from itertools import count, islice, product
def agen(): # generator of terms
    yield 2
    yield from (t for digits in count(2) for f in "1248" for mid in product("01248", repeat=digits-2) if isprime(t:=int(f + "".join(mid) + "1")))
print(list(islice(agen(), 45))) # _Michael S. Branicky_, Jun 11 2025

