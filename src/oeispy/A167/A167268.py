# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A167268

from mpmath.libmp import sqrtrem
def a(n):
    s, r = sqrtrem(n)
    return 4 * (-n % (s + (r>s))) + 2
# _Christoph B. Kassir_, Apr 07 2022

