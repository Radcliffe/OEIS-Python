# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A108731

def row(n, i=2): return [n] if n < i else [*row(n//i, i=i+1), n%i]
print([d for n in range(35) for d in row(n)]) # _Michael S. Branicky_, Oct 02 2024

