# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A243410

import sympy
from sympy import isprime
from sympy import prime
{print(prime(n),end=', ') for n in range(1,10**5) if isprime(1000*prime(n)-1) and isprime(1000*prime(n)-3) and isprime(1000*prime(n)-7) and isprime(1000*prime(n)-9)}

