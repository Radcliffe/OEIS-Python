# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A245730

from sympy import isprime
sorted([int(('0'*m+'1')*n,2) for m in range(50) for n in range(1,50) if isprime(int(('0'*m+'1')*n,2))])

