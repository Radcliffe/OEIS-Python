# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A106582

from sympy import isprime
from itertools import count, islice
def agen(): # generator of terms
    for k in count(1):
        s = str(k)
        if any(s[i] != '0' and isprime(int(s[:i])) and isprime(int(s[i:])) for i in range(1, len(s))):
            yield k
print(list(islice(agen(), 55))) # _Michael S. Branicky_, Feb 26 2022

