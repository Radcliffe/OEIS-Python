# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A163263

import heapq
def aupton(terms, verbose=False):
    p = 2*3; h = [(p, 2, 3)]; nextcount = 4; alst = []; oldv = None
    while len(alst) < terms:
        (v, s, l) = heapq.heappop(h)
        if v == oldv and ((s > oldl) or (olds > l)) and v not in alst:
            alst.append(v)
            if verbose: print(f"{v}, [= Prod_{{i = {s}..{l}}} i = Prod_{{i = {olds}..{oldl}}} i]")
        if v >= p:
            p *= nextcount
            heapq.heappush(h, (p, 2, nextcount))
            nextcount += 1
        oldv, olds, oldl = v, s, l
        v //= s; s += 1; l += 1; v *= l
        heapq.heappush(h, (v, s, l))
    return alst
print(aupton(4, verbose=True)) # _Michael S. Branicky_, Jun 24 2021

