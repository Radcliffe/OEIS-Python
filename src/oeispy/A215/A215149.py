# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A215149

def A215149(n): return n*(pow(2,n)+2)//2
print([A215149(n) for n in range(41)]) # _G. C. Greubel_, Jan 18 2025

