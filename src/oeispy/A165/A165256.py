# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A165256

# see link for alternate version producing full sequence instantly
from sympy import primefactors
def ok(n): return len(primefactors(n)) == len(str(n))
print([k for k in range(10**5) if ok(k)]) # _Michael S. Branicky_, Apr 13 2023

