# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A306508

for n in range(2,max_n):
    factor_list = numbthy.factor(n)
    numFactors = len(factor_list)
    if numFactors <= 3:
        continue
    if not bsflib.is_composite_and_square_free_with_list(n,factor_list):
        continue
    fciFactorizations = bsflib.fullyCompositeIdempotentFactorizations(n,factor_list)
    numFCIFs = len(fciFactorizations)
    if numFCIPs > 0:
        fcIdempotents += 1
    print(n)

