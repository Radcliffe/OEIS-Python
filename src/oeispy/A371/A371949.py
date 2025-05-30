# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371949

from itertools import product
from collections import Counter
from functools import lru_cache
from fractions import Fraction
def get_elims(o,d): return tuple(-''.join(['od'[int(o>d)] for o,d in zip(*[sorted(i)[-2:][::-1] for i in [o,d]])]).count(j) for j in 'od')
@lru_cache()
def elim_p(o_n,d_n): return {j:Fraction(k,7776) for j,k in Counter([get_elims(i[:o_n],i[o_n:o_n+d_n]) for i in product(range(1,7),repeat=5)]).most_common()}
@lru_cache()
def res_p(o_n,d_n): return {(o_n+i[0],d_n+i[1]):j for i,j in elim_p(min(3,o_n), min(2,d_n)).items()}
def get_final_result(o_n,d_n):
    d,g = {(o_n,d_n):1}, [(o_n,d_n)]
    while g:
        w,p = g[0], d.pop(g[0])
        for i,j in res_p(*w).items():
            d[i] = d.get(i,0)+j*p
        g = [i for i in d.keys() if min(i)>0]
    return d
def get_win_count(o_n,d_n): return (sum(j for i,j in get_final_result(o_n,d_n).items() if i[0]>i[1])*(7776**(o_n+d_n-1))).numerator
a = [get_win_count(o_n,t-o_n) for t in range(2,30) for o_n in range(1,t)]

