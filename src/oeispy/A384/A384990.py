# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A384990

from sympy.combinatorics import Permutation
def apply_transformation(seq):
    step = 1
    i = step
    while i < len(seq):
        seq.append(seq.pop(i))
        step += 1
        i += step - 1
    return seq
def a(n):
    seq = list(range(n))
    p = apply_transformation(seq.copy())
    return Permutation(p).order()

