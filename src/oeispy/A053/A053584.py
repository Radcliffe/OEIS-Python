# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A053584

from sympy import isprime
from itertools import count, islice
def agen(an=7):
    while True:
        yield an
        pow10 = 10**len(str(an))
        for t in count(pow10+an, step=pow10):
            if isprime(t):
                an = t
                break
print(list(islice(agen(), 18))) # _Michael S. Branicky_, Jun 23 2022

