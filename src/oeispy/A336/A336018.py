# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A336018

def A336018(n):
    return len(bin(n**n//(2**((len(bin(n))-3)*n))))-3 # _Chai Wah Wu_, Jul 09 2020

