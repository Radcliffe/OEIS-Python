# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A037308

def ok(n): return sum(map(int, str(n))) == sum(map(int, bin(n)[2:]))
print(list(filter(ok, range(3013)))) # _Michael S. Branicky_, Jun 20 2021

