# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A248323

from sympy import divisors
import re
A248323_list = [n for n in range(1,10**7) if len(list(re.finditer('(?='+str(n)+')',''.join([str(d) for d in divisors(n)])))) > 1]
# _Chai Wah Wu_, Nov 01 2014

