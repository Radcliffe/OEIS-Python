# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A273154

from itertools import product
def qf(s):
    for l in range(1, len(s)//4 + 1):
      for i in range(len(s) - 4*l + 1):
          if s[i:i+l] == s[i+l:i+2*l] == s[i+2*l:i+3*l] == s[i+3*l:i+4*l]:
              return False
    return True
def a(n):
    if n == 0: return 1
    return 2*sum(1 for w in product("01", repeat=n-1) if qf("0"+"".join(w)))
print([a(n) for n in range(21)]) # _Michael S. Branicky_, Mar 14 2022

