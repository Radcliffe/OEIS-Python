# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A127050

from itertools import islice, count
def A127050gen(): return islice((int(d) for n in count(0) for d in str(n)),1,None,2)
A127050_list = list(islice(A127050gen(),40)) # _Chai Wah Wu_, Dec 04 2021

