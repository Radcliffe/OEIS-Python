# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A092062

# uses A061015gen() and imports from A061015
from sympy import isprime
def agen():
    yield from (k for k, ak in enumerate(A061015gen(), 1) if isprime(ak))
print(list(islice(agen(), 5))) # _Michael S. Branicky_, Jun 27 2022

