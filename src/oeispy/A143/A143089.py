# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A143089

from sympy import cacheit
@cacheit
def A143089(n):
    if n <= 1:
        return 1
    else:
        return A143089(n-A143089(n-1))+A143089(2*n//3)
print([A143089(n) for n in range(40)]) # Oct 18 2009

