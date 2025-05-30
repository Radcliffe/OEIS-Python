# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A032378

from itertools import count, islice
from sympy import integer_nthroot
def A032378_gen(): # generator of terms
    return filter(lambda x: not x%integer_nthroot(x,3)[0],(n+(k:=integer_nthroot(n, 3)[0])+int(n>=(k+1)**3-k) for n in count(1)))
A032378_list = list(islice(A032378_gen(),40)) # _Chai Wah Wu_, Oct 12 2024

