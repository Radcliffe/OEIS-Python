# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A236045

import sympy
from sympy import isprime
{print(p) for p in range(10**8) if isprime(p) and isprime(p**1+p+1) and isprime(p**2+p+1) and isprime(p**3+p+1) and isprime(p**4+p+1)}

