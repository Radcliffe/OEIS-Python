# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A081960

from functools import reduce
import operator
def a(n): return reduce(operator.mul, row(n), 1) # row(n) is given in A081957. - _James Rayman_, Jan 18 2021

