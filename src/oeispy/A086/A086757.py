# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A086757

from sympy import sieve
from sympy.ntheory import is_palindromic
def a086757(n): return next(p for p in sieve if is_palindromic(n, p)) # _Dumitru Damian_, Jan 29 2024

