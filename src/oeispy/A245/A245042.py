# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A245042

import sympy
L = (k**2 + 4 for k in range(10**3))
[n//5 for n in L if n % 5 == 0 and sympy.ntheory.isprime(n//5)]

