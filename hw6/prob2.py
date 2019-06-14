from __future__ import print_function, division
import numpy as np
from sisl import *
import matplotlib.pyplot as plt

n=3
graphene = geom.graphene().tile(n, 0).tile(n, 1)

print(graphene)
plot(graphene)

xyz_center = graphene.center(what='xyz')
index = graphene.close(xyz_center, 1.5)
index = index[0]
system = graphene.remove(index)

H = Hamiltonian(system)
print(H)

r = (0.1,  1.44)
t = (0. , -2.7 )
H.construct([r, t])

band = BandStructure(H, [[0, 0, 0], [0, 0.5, 0],
                         [1/3, 2/3, 0], [0, 0, 0]], 400,
                        [r'$\Gamma$', r'$M$',
                         r'$K$', r'$\Gamma$'])

fig,ax=plt.subplots(figsize=(8,8))
bs = band.asarray().eigh()
lk, kt, kl = band.lineark(True)
ax.set_xticks(kt)
ax.set_xticklabels(kl)
ax.set_xlim(0, lk[-1])
ax.set_ylim([-3, 3])
ax.set_ylabel('$E-E_F$ [eV]')
for bk in bs.T:
    ax.plot(lk, bk)

plt.show()
