# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A359997

import networkx as nx
from collections import Counter
def F(n): return nx.DiGraph(((0,0),(0,1),(1,0))) if n == 1 else nx.line_graph(F(n-1))
def A359997_row(n):
    a = Counter(len(c) for c in nx.simple_cycles(F(n)))
    return [a[k] for k in range(1,max(a)+1)]

