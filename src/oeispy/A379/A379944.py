# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A379944

import math
from sympy import isprime
def a(n):
    factorial = str(math.factorial(n))
    for d in range(1, len(factorial)+1):
        if isprime(int(factorial[:d])):
            return d
    return 0

