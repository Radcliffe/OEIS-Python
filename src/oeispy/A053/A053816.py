# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A053816

def is_A053816(n): return n==sum(divmod(n**2,10**len(str(n)))) and n
print(upto_1e5:=list(filter(is_A053816, range(10**5)))) # _M. F. Hasler_, Mar 28 2025

