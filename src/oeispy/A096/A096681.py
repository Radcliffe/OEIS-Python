# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A096681

def next02(n):
  s = str(n)
  if s > '2'*len(s): return int('2' + '0'*len(s))
  for i, c in enumerate(s):
    if c == '1': return int(s[:i] + '2' + '0'*(len(s)-i-1))
    elif s[i:] > '2'*(len(s)-i): return int(s[:i-1] + '2' + '0'*(len(s)-i))
def a(n):
  k = 1
  while set(str(k*n)) - set('02') != set(): k = max(k+1, next02(k*n)//n)
  return k
print([a(n) for n in range(1, 51)]) # _Michael S. Branicky_, Feb 01 2021

