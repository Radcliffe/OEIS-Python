# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A094416

# The Akiyama-Tanigawa algorithm applied to the powers of r + 1
# generates the rows. Adds one row (r=0) and one column (n=0).
# Adapted from Peter Luschny on A371568.
def f(n, r): return (r + 1)**n
def ATtransform(r, len, f):
  A = [0] * len
  R = [0] * len
  for n in range(len):
      R[n] = f(n, r)
      for j in range(n, 0, -1):
          R[j - 1] = j * (R[j] - R[j - 1])
      A[n] = R[0]
  return A
for r in range(8): print([r], ATtransform(r, 8, f)) # _Shel Kaphan_, May 03 2024

