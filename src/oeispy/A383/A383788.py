# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383788

def a(n): return int("".join(d if d<"5" else str(9-int(d)) for d in str(n)))
print([a(n) for n in range(1, 78)]) # _Michael S. Branicky_, May 10 2025

