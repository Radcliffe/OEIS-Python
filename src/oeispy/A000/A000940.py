# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A000940

from sympy import factorial, divisors, totient
def A000940(n): return 1 if n == 3 else ((sum(totient(m:=n//d)**2*factorial(d)*m**d for d in divisors(n,generator=True))+(1<<(k:=n>>1)-2)*n*(n<<2 if n&1 else (n+6))*factorial(k))>>2)//n//n # _Chai Wah Wu_, Nov 07 2022

