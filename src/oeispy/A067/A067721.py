# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A067721

from itertools import takewhile
from collections import deque
from sympy import divisors
def A067721(n): return ((a:=next(iter(deque((d for d in takewhile(lambda d:d<n, divisors(n**2)) if not (d-n**2//d)&3),1)),0))+(n**2//a-(n<<1) if a else 0)>>2) if n else 1 # _Chai Wah Wu_, Aug 21 2024

