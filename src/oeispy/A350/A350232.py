# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350232

from itertools import count, islice
def A350232gen(): return filter(lambda n:(m := int(str(n)[::-1])) % 4 and not m % 5,filter(lambda n: n % 5 and not n % 4,count(1)))
A350232_list = list(islice(A350232gen(),20)) # _Chai Wah Wu_, Dec 21 2021

