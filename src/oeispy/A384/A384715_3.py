# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A384715

def a(n: int) -> int:  # after _Chai Wah Wu_
    b = bin(n)[2:]; p = b.count("10"); q = b.count("11")
    return (p + (2 if q else 1)) * 2**n.bit_count()  # _Peter Luschny_, Jun 25 2025

