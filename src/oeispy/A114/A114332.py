# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A114332

def a(n):
    if n == 0: return 15 # zerO
    if n%1000000 == 0: return 14 # millioN, billioN, ...
    r = n%100
    if r == 0: return 4 # hundreD, thousanD
    if r == 12: return 5 # twelvE
    if 10 <= r < 20: return 14 # teN, eleveN, thirteeN, ..., nineteeN
    return [25, 5, 15, 5, 18, 5, 24, 14, 20, 5][n%10] # *Y, *onE, ..., *ninE
print([a(n) for n in range(101)]) # _Michael S. Branicky_, Jan 19 2022

