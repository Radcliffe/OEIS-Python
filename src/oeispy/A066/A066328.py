# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A066328

from sympy import primepi, primefactors
def A066328(n): return sum(map(primepi,primefactors(n))) # _Chai Wah Wu_, Mar 13 2024

