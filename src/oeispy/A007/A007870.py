# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A007870

from sympy import prod
from sympy.utilities.iterables import ordered_partitions
a = lambda n: prod(map(prod, ordered_partitions(n))) if n > 0 else 1
print([a(n) for n in range(0, 12)]) # _Darío Clavijo_, Feb 22 2024

