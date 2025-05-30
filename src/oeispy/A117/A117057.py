# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A117057

from operator import mul
from functools import reduce
from gmpy2 import t_mod, mpz
A117057 = sorted([mpz(n) for n in (str(x)+str(x)[::-1] for x in range(1,10**6))
        if not (n.count('0') or t_mod(mpz(n), reduce(mul,(mpz(d) for d in n))))]+
        [mpz(n) for n in (str(x)+str(x)[-2::-1] for x in range(10**6))
        if not (n.count('0') or t_mod(mpz(n), reduce(mul,(mpz(d) for d in n))))])
# _Chai Wah Wu_, Aug 26 2014

