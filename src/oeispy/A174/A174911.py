# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A174911

from gmpy2 import is_prime
from itertools import count, islice
def agen(): # generator of terms
    alst = [1]
    yield 1
    for m in count(2):
        if all(not is_prime(m-ai+1) for ai in alst):
            alst.append(m)
            yield alst[-1]
print(list(islice(agen(), 50))) # _Michael S. Branicky_, Oct 13 2024

