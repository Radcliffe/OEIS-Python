# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A083058

def a(n): return n - n.bit_length() + (n == 1)  # _Matthew Andres Moreno_, Jan 04 2024

