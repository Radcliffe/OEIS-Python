# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A243400

import sympy
from sympy import isprime
{print(n,end=', ') for n in range(10**4) if isprime(n**6-n**5-n**4-n**3-n**2-n-1) and isprime(n)}

