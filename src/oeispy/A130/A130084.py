# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A130084

from sympy import integer_nthroot
def A130084(n): return (lambda x:x[0]+(not x[1]))(integer_nthroot(10**(n-1),10)) # _Chai Wah Wu_, Jun 20 2024

