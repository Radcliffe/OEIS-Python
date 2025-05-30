# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A373082

def count_zero_runs_in_binary(n):
    binRep = bin(n)[2:]   # as binary, but ignore "0b" prefix
    zRuns = binRep.split('1')  # split on the 1's
    zRvec = [run for run in zRuns if run] # filter "" to get runs of 0
    return len(zRvec)
out = []
for i in range(100):
    gv = i ^ (i>>1)   # gray code
    ans = count_zero_runs_in_binary(gv)
    out.append(ans)
print(out)

