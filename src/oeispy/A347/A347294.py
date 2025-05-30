# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A347294

from sympy import isprime, factorint
from itertools import count, islice, product
def f(s): return s[::-1].translate({ord("6"):ord("9"), ord("9"):ord("6")})
def agen():
    for digits in count(3):
        for first in "1689":
            for mid in product("01689", repeat=digits-2):
                for last in "19":
                    s = first + "".join(mid) + last
                    t = int(s)
                    if isprime(t):
                        flip = f(s)
                        if sum(factorint(int(flip)).values()) == 2:
                            yield t
print(list(islice(agen(), 41))) # _Michael S. Branicky_, Feb 16 2024

