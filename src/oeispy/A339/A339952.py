# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A339952

def aupto(limit):
  m = int(limit**.5) + 2
  es = [i*i for i in range(2, m, 2)]
  os = [i*i for i in range(1, m, 2)]
  return sorted(set(a+b for a in es for b in os if a+b <= limit))
print(aupto(377)) # _Michael S. Branicky_, May 13 2021

