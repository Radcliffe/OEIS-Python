# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342996

from sympy import primorial
from sympy.functions import partition
def A342996(n): return partition(primorial(n)) if n > 0 else 1 # _Chai Wah Wu_, Apr 03 2021

