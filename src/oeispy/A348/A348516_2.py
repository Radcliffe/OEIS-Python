# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A348516

from gmpy2 import digits
def A348516(n):
    k, s = 1, digits(n,3).rstrip('0')
    if s == '1' or s == '': return 1-len(s)
    m = int(s,3)
    mk = m
    while s.count('1') != s.count('2'): k += 1; mk *= m; s = digits(mk,3)
    return k # _Chai Wah Wu_, Nov 11 2021

