# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A028982

from itertools import count, islice
from sympy.ntheory.primetest import is_square
def A028982_gen(startvalue=1): # generator of terms >= startvalue
    return filter(lambda n:int(is_square(n) or is_square(n<<1)),count(max(startvalue,1)))
A028982_list = list(islice(A028982_gen(),30)) # _Chai Wah Wu_, Jan 09 2023

