# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A229836

from math import factorial
from sympy import primepi
def A229836(n): return primepi(n**n)-primepi(factorial(n)-1) # _Chai Wah Wu_, Jun 06 2024

