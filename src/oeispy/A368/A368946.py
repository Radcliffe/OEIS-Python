# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A368946

from itertools import islice
def occurrence_swaps(w, s, t):
    out, oi = [], w.find(s)
    while oi != -1:
        out.append(w[:oi] + t + w[oi+len(s):])
        oi = w.find(s, oi+1)
    return out
def moves(w): # moves for word w in MIU system, encoded as 310
    nxt = []
    if w[-1] == '1': nxt.append(w + '0')        # Rule 1
    if w[0] == '3': nxt.append(w + w[1:])       # Rule 2
    nxt.extend(occurrence_swaps(w, '111', '0')) # Rule 3
    nxt.extend(occurrence_swaps(w, '00', ''))   # Rule 4
    return nxt
def agen(): # generator of terms
    frontier = ['31']
    while len(frontier) > 0:
        yield from [int(t) for t in frontier]
        reach1 = [m for p in frontier for m in moves(p)]
        frontier, reach1 = reach1, []
print(list(islice(agen(), 28))) # _Michael S. Branicky_, Jan 14 2024

