# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A354408

from sympy import Matrix
def A354408(n,k):
    return Matrix(n,n,lambda i,j:int(i!=j and i!=(j+k)%n)).per() # _Pontus von Brömssen_, May 31 2022

