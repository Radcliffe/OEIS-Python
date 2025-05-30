# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A344683

from sympy import divisors as div, totient as phi
def D(f, g, n):
    return sum(f(d)*g(n//d) for d in div(n))
def phi_o_phi(n):
    return D(phi, phi, n)
def a(n):
    return D(phi, phi_o_phi, n)

