# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A278679

## by Taylor expansion
from sympy import *
from sympy.abc import z
h = (exp(sqrt(2)*z) * (4*z-4) - (sqrt(2)-2)*exp(2*sqrt(2)*z) + sqrt(2) + 2) / ((sqrt(2)-2)*exp(sqrt(2)*z) + 2 + sqrt(2))**2
NUMBER_OF_COEFFS = 20
coeffs = Poly(series(h,n = NUMBER_OF_COEFFS)).coeffs()
coeffs.reverse()
## and remove first coefficient 1 that corresponds to O(n**k)
coeffs.pop(0)
print([coeffs[n]*factorial(n+2) for n in range(len(coeffs))])

