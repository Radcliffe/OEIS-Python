# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A303610

def closer(pos1, pos2):
    dpos1 = (pos1[0]**2.0+pos1[1]**2.0)**.5
    dpos2 = (pos2[0]**2.0+pos2[1]**2.0)**.5
    if (1.0-dpos1)**2.0 < (1.0-dpos2)**2.0:
        return True
    else:
        return False
def converts(path):
    return ''.join(path)
l = []
for steps in range(1, 20):
    stepsize = 1.0/steps
    pos = [-1.0, 0.0]
    paths = []
    for i in range(0, 2*steps):
        if closer([pos[0]+stepsize, pos[1]], [pos[0], pos[1]+stepsize]):
            pos = [pos[0]+stepsize, pos[1]]
            paths.append(str(0))
        else:
            pos = [pos[0], pos[1]+stepsize]
            paths.append(str(1))
    l.append(int(converts(paths)))
print(l)

