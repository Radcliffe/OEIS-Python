# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A263299

from gmpy2 import is_prime
A263299_list = [n for n in (int('1'*k+str(k*(k+1)+1)+'1'*k) for k in range(10**2)) if is_prime(n)] # _Chai Wah Wu_, Oct 19 2015

