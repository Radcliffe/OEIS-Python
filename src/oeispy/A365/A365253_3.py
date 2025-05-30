# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A365253

from re import compile
def A365253(n):
    if n == 0: return 1
    r = compile(r'(.)(.*)\1\2\1\2\1')
    return 2*sum(not r.search(format(k,f'0{n}b')) for k in range(2**(n-1))) # _Pontus von Brömssen_, Aug 29 2023

