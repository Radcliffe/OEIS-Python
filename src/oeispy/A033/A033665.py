# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A033665

A033665 = lambda n, LIM=333: next((i for i in range(LIM) if is_A002113(n) or not(n := A004086(n)+n)), -1) # The second, optional argument is a search limit, see above. - _M. F. Hasler_, May 23 2024

