# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A178354

def digpow(s): return sum(int(d)**i for i, d in enumerate(s, start=1))
def aupto(limit):
  alst = []
  for k in range(1, limit+1):
    s = str(k)
    if digpow(s) == digpow(s[::-1]): alst.append(k)
  return alst
print(aupto(454)) # _Michael S. Branicky_, Mar 23 2021

