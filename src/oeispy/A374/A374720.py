# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A374720

from sympy.combinatorics.permutations import Permutation
def ks(s):
  j, S = 0, list(range(s))
  for i in range(s):
    j = (i + j + 1 + S[i]) % s
    S[i], S[j] = S[j], S[i]
  return S
def a(n): return Permutation(ks(n)).rank()
print([a(n) for n in range(1, 21)])

