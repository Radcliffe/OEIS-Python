# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A165317

def a(n): return ((n^(n<<1))&(n^(n>>1))).bit_count() + ((n&3)==2)
print([a(n) for n in range(1, 106)]) # _Michael S. Branicky_, May 12 2024

