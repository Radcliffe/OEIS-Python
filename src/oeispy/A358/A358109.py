# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A358109

from sympy import binomial, S
def A358109(n): return (1<<(n<<2))*sum(binomial(S.Half,k)**2*binomial(n,k) for k in range(n+1)) # _Chai Wah Wu_, Nov 13 2022

