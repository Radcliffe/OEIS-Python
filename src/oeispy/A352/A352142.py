# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352142

from itertools import count, islice
from sympy import primepi, factorint
def A352142_gen(startvalue=1): # generator of terms >= startvalue
    return filter(lambda k:all(map(lambda x:x[1]%2 and primepi(x[0])%2, factorint(k).items())),count(max(startvalue,1)))
A352142_list = list(islice(A352142_gen(),30)) # _Chai Wah Wu_, Mar 18 2022

