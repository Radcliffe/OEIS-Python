# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A295025

def ok(cube): return max(str(cube)) == "5"
print([c for c in (i**3 for i in range(1370)) if ok(c)]) # _Michael S. Branicky_, Dec 05 2021

