# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A016173

def A016173(n): return (pow(10,n+1) - pow(6,n+1))//4
print([A016173(n) for n in range(41)]) # _G. C. Greubel_, Nov 13 2024

