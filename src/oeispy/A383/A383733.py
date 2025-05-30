# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383733

# Illustrative brute-force check for small n using networkx
import networkx as nx
from itertools import product
def Cn_k_graph(n, k):
    G = nx.cycle_graph(n)
    for i in range(n):
        G.add_edge(i, (i+k)%n)
    if n % 2 == 0:
        for i in range(n//2):
            G.add_edge(i, i+n//2)
    return G
def count_colorings(G, colors=3):
    nodes = list(G.nodes())
    count = 0
    for coloring in product(range(colors), repeat=len(nodes)):
        if all(coloring[u] != coloring[v] for u,v in G.edges()):
            count += 1
    return count
# Example usage:
for n in range(6, 21):
    G = Cn_k_graph(n, 3)
    print(f'n={n}, colorings={count_colorings(G)}')

