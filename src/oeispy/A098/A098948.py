# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A098948

def ok(n): return set("13579") & set(str(n)) == {'7'}
print(list(filter(ok, range(727)))) # _Michael S. Branicky_, Jul 27 2021

