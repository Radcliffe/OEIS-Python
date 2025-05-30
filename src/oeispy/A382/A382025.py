# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A382025

from sympy import binomial
from sympy.utilities.iterables import partitions
from sympy.combinatorics.partitions import IntegerPartition
kinds = 3 - 1   # the number of part kinds - 1
def a382025_row( n):
    if n == 0 : return [1]
    t = list( [0] * n)
    for p in partitions( n):
        p = IntegerPartition( p).as_dict()
        fact = 1
        s = 0
        for k in p :
            s += p[k]
            fact *= binomial( kinds + p[k], kinds)
        if s > 0 :
            t[s - 1] += fact
    for i in range( n - 1):
        t[i+1] += t[i]
    return [0] + t

