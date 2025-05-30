# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383977

def fib(n):
  return n if n < 2 else fib(n - 1) + fib(n - 2)
def a_first(n):
  # returns an array of the first n terms
  if n == 0: return []
  f = []
  i = 1
  while True:
    for j in range(fib(i) - 1):
      f.append(f[j] + fib(i + 1))
      if len(f) == n: return f
    f.append(fib(i + 1))
    if len(f) == n: return f
    i += 1

