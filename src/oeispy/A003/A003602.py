# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A003602

import math
def a(n): return (n/2**int(math.log(n - (n & n - 1), 2)) + 1)/2 # _Indranil Ghosh_, Apr 24 2017

