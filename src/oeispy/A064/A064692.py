# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A064692

def A064692(n):
    x=str(n)
    return x.count("0")+x.count("4")+x.count("6")+x.count("8")*2+x.count("9") # _Indranil Ghosh_, Feb 02 2017

