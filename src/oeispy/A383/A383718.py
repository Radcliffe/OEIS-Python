# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A383718

from itertools import groupby
from math import prod, factorial as fact
rlenomial=lambda n: fact(l:=n.bit_length())//prod(map(lambda n: fact(len(list(n[1]))),groupby(map(lambda i: n>>i&1,range(l)))))

