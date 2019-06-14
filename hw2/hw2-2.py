import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-np.pi,np.pi,10000)
y1=2*np.sqrt(0.01+(np.cos(x/2))**2)
y2=-y1
fig,ax=plt.subplots(figsize=(8,8))
ax.plot(x,y1)
ax.plot(x,y2)
ax.set_title(r"Energy Dispersion for Diatomic Chain")
ax.set_xlabel(r"Wavevector $k$ * lattice constant $a$")
ax.set_ylabel("Energy units of |t|")
ax.set_xlim((-np.pi,np.pi))
#  ax.set_ylim((0,None))

fig.savefig("result_a.png")

s=0.2
alpha=np.sqrt(1+2*s*np.cos(x/2))
beta=np.sqrt(1-2*s*np.cos(x/2))

y1=4*s*(np.cos(x/2))**2+np.sqrt(16*(s**2)*(np.cos(x/2)**4)-(16*(s**2)-4)*(np.cos(x/2)**2)+0.04*(alpha**2)*(beta**2))
y2=4*s*(np.cos(x/2))**2-np.sqrt(16*(s**2)*(np.cos(x/2)**4)-(16*(s**2)-4)*(np.cos(x/2)**2)+0.04*(alpha**2)*(beta**2))

fig,ax=plt.subplots(figsize=(8,8))
ax.plot(x,y1)
ax.plot(x,y2)
ax.set_title(r"Energy Dispersion for Diatomic Chain (s=0.2)")
ax.set_xlabel(r"Wavevector $k$ * lattice constant $a$")
ax.set_ylabel("Energy units of |t|")
ax.set_xlim((-np.pi,np.pi))

fig.savefig("result_c.png")
