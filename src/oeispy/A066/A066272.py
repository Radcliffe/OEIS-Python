# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A066272

from sympy import divisors
def A066272(n):
    return len([d for d in divisors(2*n) if n > d >=2 and n%d]) +  len([d for d in divisors(2*n-1) if n > d >=2 and n%d]) +  len([d for d in divisors(2*n+1) if n > d >=2 and n%d]) # _Chai Wah Wu_, Aug 11 2014

