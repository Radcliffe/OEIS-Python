# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A247358

from itertools import chain
A247358_list = list(chain.from_iterable(sorted((b+1)**(n-b) for b in range(n)) for n in range(1,8))) # _Chai Wah Wu_, Sep 14 2014

