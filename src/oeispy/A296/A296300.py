# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A296300

[n for n in range(1, 100000) if all(n%k == 0 or n**(1/k) >= int(n**(1/(k-1))) for k in range(2, len(bin(n))-1))]

