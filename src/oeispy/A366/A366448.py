# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A366448

def A366448(n): return len({(a+d,a*d-b*c) for a in range(n+1) for b in range(n+1) for c in range(b+1) for d in range(a+1)}) # _Chai Wah Wu_, Oct 12 2023

