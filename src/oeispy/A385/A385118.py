# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A385118

from itertools import product
def a(n): return sum((x*x+y*y+z*z-3*x*y*z)%n == 0 for x,y,z in product(range(n), repeat=3))
print([a(n) for n in range(1, 51)])

