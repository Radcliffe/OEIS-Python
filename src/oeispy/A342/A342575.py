# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342575

def a(n):
  k, twok, target = n+1, 2**(n+1), str(2**n)
  while target not in str(twok): k, twok = k+1, twok*2
  return k
print([a(n) for n in range(27)]) # _Michael S. Branicky_, Mar 16 2021

