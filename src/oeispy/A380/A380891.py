# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A380891

import gmpy2
def a(n): return int(gmpy2.iroot(n**4 if n&1 else n, 3)[0])

