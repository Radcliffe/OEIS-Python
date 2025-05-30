# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A333325

def a333325(n):
  seq = []
  for k in range(n):
    options = []
    l = len(seq) + 1
    for m in range(3): # base
      for i in range(l // 2, -1, -1):
        if seq[l - 2 * i: l - i] == seq[l - i:] + [m]: break
      options.append(2 * i)
    seq.append(options.index(min(options)))
  return seq
print(a333325(81))

