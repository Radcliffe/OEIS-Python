# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A333447

from functools import lru_cache
@lru_cache(maxsize=None)
def A333447(n): return (1<<((m:=1<<n)<<1)-1)-(k:=1<<m-1)+(k+1)*A333447(n-1) if n else 2 # _Chai Wah Wu_, Nov 23 2023

