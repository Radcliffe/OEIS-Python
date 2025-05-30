# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A370448

import sympy, functools
from numpy.lib.stride_tricks import sliding_window_view as rolling
binomial_sym_sympy = lambda L, R : sympy.functions.combinatorial.factorials.binomial(L+R, L)
@functools.cache
def C_analytic(L, R):
    return binomial_sym_sympy(L, R) * P_analytic(L) * P_analytic(R)
@functools.cache
def P_analytic(n):
    _zero, _one, _x = sympy.core.numbers.Zero(), sympy.core.numbers.One(), sympy.symbols("x")
    if n == 0: return _one
    # provide analytic expressions for the functions to integrate and the bounds of them
    int_bounds = [_zero, *[1/(1 + C_analytic(L+1, n-L-2)/C_analytic(L, n-L-1)) for L in range(n-1)], _one]
    int_polys = [sympy.poly(C_analytic(L, n-1-L) * _x**L * (1-_x)**(n-1-L), _x, domain="Q").integrate() for L in range(n)]
    int_summands = [int_poly(R_bound)-int_poly(L_bound) for int_poly, (L_bound, R_bound) in zip(int_polys, rolling(int_bounds, 2))]
    return sum(int_summands)
def A370448(n): return P_analytic(n).numerator

