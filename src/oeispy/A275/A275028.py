# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A275028

from itertools import count, islice
from sympy.ntheory.primetest import is_square
def A275028_gen(): # generator of terms
    r, t = ''.maketrans('69','96'), set('0125689')
    for l in count(1):
        if l%10:
            m = l**2
            if set(s:=str(m)) <= t and is_square(int(s[::-1].translate(r))):
                yield m
A275028_list = list(islice(A275028_gen(),10)) # _Chai Wah Wu_, Apr 09 2024

