# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A075113

def A075113(n: int) -> int:
    s = bin(n)[2:]
    return n * (n + 1) // 2 - int(s + s[::-1], 2) // 3
print([A075113(n) for n in range(69)]) # _Peter Luschny_, Dec 14 2022

