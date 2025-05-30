# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A364724

from itertools import count, islice
from sympy import sqrt_mod_iter, discrete_log
def A364724_gen(): # generator of terms
    yield 0
    for k in count(2):
        m = None
        for d in sqrt_mod_iter(-3,k):
            r = d>>1 if d&1 else d+k>>1
            try:
                m = discrete_log(k,r,2) if m is None else min(m,discrete_log(k,r,2))
            except:
                continue
        if m is not None: yield m
A364724_list = list(islice(A364724_gen(),30))

