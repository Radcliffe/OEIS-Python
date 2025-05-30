# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A067836

from sympy import nextprime
def A067836_gen(): # generator of terms
    a, f = 2, 1
    yield 2
    while True:
        yield (a:=nextprime((f:=f*a)+1)-f)
A067836_list = list(islice(A067836_gen(),30)) # _Chai Wah Wu_, Sep 09 2023

