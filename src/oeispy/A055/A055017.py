# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A055017

def A055017(n): return sum((-1 if i % 2 else 1)*int(j) for i, j in enumerate(str(n)[::-1])) # _Chai Wah Wu_, May 11 2022

