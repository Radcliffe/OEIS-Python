# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A000164

import collections; a = collections.Counter(i*i + j*j + k*k for i in range(100) for j in range(i+1) for k in range(j+1)) # _David Radcliffe_, Apr 15 2019

