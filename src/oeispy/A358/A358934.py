# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A358934

from sympy import fibonacci
def a(n):
    return fibonacci(n+1)**5-fibonacci(n-1)**5

