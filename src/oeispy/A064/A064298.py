# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A064298

# Using graphillion
from graphillion import GraphSet
import graphillion.tutorial as tl
def A064298(n, k):
    if n == 1 or k == 1: return 1
    universe = tl.grid(n - 1, k - 1)
    GraphSet.set_universe(universe)
    start, goal = 1, k * n
    paths = GraphSet.paths(start, goal)
    return paths.len()
print([A064298(j + 1, i - j + 1) for i in range(11) for j in range(i + 1)])  # _Seiichi Manyama_, Apr 06 2020

