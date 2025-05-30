# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A112676

# Using graphillion
from graphillion import GraphSet
def make_n_triangular_grid_graph(n):
    s = 1
    grids = []
    for i in range(n + 1, 1, -1):
        for j in range(i - 1):
            a, b, c = s + j, s + j + 1, s + i + j
            grids.extend([(a, b), (a, c), (b, c)])
        s += i
    return grids
def A112676(n):
    if n == 1: return 1
    universe = make_n_triangular_grid_graph(n - 1)
    GraphSet.set_universe(universe)
    cycles = GraphSet.cycles(is_hamilton=True)
    return cycles.len()
print([A112676(n) for n in range(1, 12)])  # _Seiichi Manyama_, Nov 30 2020

