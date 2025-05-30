# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A085780

from itertools import count, islice
from sympy import divisors, integer_nthroot
def A085780_gen(startvalue=0): # generator of terms
    if startvalue <= 0:
        yield 0
    for n in count(max(startvalue,1)):
        for d in divisors(m:=n<<2):
            if d**2 > m:
                break
            if integer_nthroot((d<<2)+1,2)[1] and integer_nthroot((m//d<<2)+1,2)[1]:
                yield n
                break
A085780_list = list(islice(A085780_gen(),10)) # _Chai Wah Wu_, Aug 28 2022

