# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A008935

a = lambda n: sum(((k+1)**2) * ((n >> k) & 1) for k in range(0, n.bit_length()))
print([a(n) for n in range(1,68)]) # _Darío Clavijo_, Dec 27 2024

