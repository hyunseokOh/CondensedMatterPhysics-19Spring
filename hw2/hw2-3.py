import numpy as np
import matplotlib.pyplot as plt

def energy(kx,ky):
    t=3
    return t*np.sqrt(1+4*(np.cos(kx/2)**2)+4*np.cos(kx/2)*np.cos(np.sqrt(3)/2*ky))

pnt=10000
pnt1=int(np.round(np.sqrt(3)*pnt))
pnt2=pnt
pnt3=2*pnt

kx1=np.linspace(0,np.pi,pnt1)
ky1=kx1/np.sqrt(3)
kx2=np.linspace(np.pi,4/3*np.pi,pnt2)
ky2=-np.sqrt(3)*kx2+4/np.sqrt(3)*np.pi
kx3=np.linspace(4/3*np.pi,0,pnt3)
ky3=0

E1_cond=energy(kx1,ky1)
E1_val=-energy(kx1,ky1)
E2_cond=energy(kx2,ky2)
E2_val=-energy(kx2,ky2)
E3_cond=energy(kx3,ky3)
E3_val=-energy(kx3,ky3)

E_cond=np.hstack([E1_cond, E2_cond, E3_cond])
E_val=np.hstack([E1_val, E2_val, E3_val])

x=np.linspace(0, pnt1+pnt2+pnt3, pnt1+pnt2+pnt3)

fig,ax=plt.subplots(figsize=(8,8))
ax.plot(x,E_cond)
ax.plot(x,E_val)
ax.set_title("Energy Dispersion of Graphene")
ax.axvline(x=pnt1,color='k',linewidth=1)
ax.axvline(x=pnt1+pnt2,color='k',linewidth=1)
ax.set_xlabel(r"Reciprocal Position")
ax.set_ylabel(r"$E$ [$eV$]")
ax.set_xlim(0,pnt1+pnt2+pnt3)
ax.set_xticks([0,pnt1,pnt1+pnt2,pnt1+pnt2+pnt3])
ax.set_xticklabels([r"$\Gamma$",r'$M$',r'$K$',r"$\Gamma$"])
ax.legend(["Conduction Band","Valence Band"])
fig.savefig("Result.png")
plt.show()

