# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A375187

from collections import Counter
from sympy import factorint
def A375187(n): return 1<<sum(e&1^1 for e in sum((Counter(factorint(m)) for m in range(2,n+1)),start=Counter()).values()) # _Chai Wah Wu_, Aug 03 2024

