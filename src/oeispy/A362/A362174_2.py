# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362174

from math import factorial
from functools import lru_cache
@lru_cache(maxsize=None)
def A362174(n): return A362174(n-1)*(2*n-1)*factorial(2*n-2)**2//n//factorial(n-1)**3//(n-1)**(n-1) if n else 1 # _Chai Wah Wu_, Jun 26 2023

