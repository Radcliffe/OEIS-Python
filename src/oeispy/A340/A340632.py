# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340632

def a(n): return (1<<n.bit_length()) - (n&-n) if n else 0

