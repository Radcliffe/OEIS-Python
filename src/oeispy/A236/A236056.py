# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A236056

import sympy
from sympy import isprime
{print(p) for p in range(10**6) if isprime(p**2+p+1) and isprime(p**2-p+1) and isprime(p**2+p-1) and isprime(p**2-p-1)}

