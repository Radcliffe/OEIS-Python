# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355616

from fractions import Fraction
from itertools import chain
def compute(n):
    marks = [[(a, b) for a in range(0, b + 1)] for b in range(1, n + 1)]
    marks = sorted(set([Fraction(a, b) for a, b in chain(*marks)]))
    dist = [(y - x) for x, y in zip(marks, marks[1:])]
    return len(set(dist))

