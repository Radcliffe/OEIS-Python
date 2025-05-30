# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A375025

from functools import cache
@cache
def Trow(n):
    if n == 0: return [1]
    if n == 1: return [-2, 1]
    fli = Trow(n - 1)
    row = [1] * (n + 1)
    row[n - 1] = -2
    for k in range(n - 2, 0, -1):
        row[k] = fli[k - 1] - fli[k + 1]
    row[0] = -2 * fli[0] - fli[1]
    return row
# _Peter Luschny_, Aug 18 2024

