# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A082806

from sympy import isprime
A082806 = sorted([n for n in chain(map(lambda x:int(str(x)+str(x)[::-1]),range(1,10**5)),map(lambda x:int(str(x)+str(x)[-2::-1]), range(1,10**5))) if isprime(n) and isprime(sum([int(d) for d in str(n)]))])
# _Chai Wah Wu_, Aug 12 2014

