# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A279515

from math import lcm
def a(n): return format(lcm(*range(1, n+1)), 'b').count('0') # _David Radcliffe_, May 22 2025

