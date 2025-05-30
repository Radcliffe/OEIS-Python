# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A298638

#Digital sum of n.
def ds(n):
  if n < 10:
    return n
  return n % 10 + ds(n//10)
def A298638(term_count):
  seq = []
  m = 0
  n = 1
  while n <= term_count:
    s = ds(m)
    r = ((m - 1) % 9) + 1 if m else 0
    if s % 2 != r % 2:
      seq.append(m)
      n += 1
    m += 1
  return seq
print(A298638(100))

