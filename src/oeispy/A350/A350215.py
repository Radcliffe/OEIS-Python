# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350215

def c(b): return not "11" in b and not "101" in b
def auptod(digits):
    return [int(b) for b in (bin(k)[2:] for k in range(2**digits)) if c(b)]
print(auptod(9)) # _Michael S. Branicky_, Dec 20 2021

