# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A177902

def ok(n): return all(di!=0 and (n-i)%di==0 for i, di in enumerate(map(int, str(n)), 1))
print([k for k in range(9000) if ok(k)]) # _Michael S. Branicky_, Feb 20 2023

