# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A283774

import math
from sympy import sqrt
r = (3 + sqrt(5))/2
[n for n in range(1, 351) if int(math.floor(n*r))%3==2] # _Indranil Ghosh_, Mar 21 2017

