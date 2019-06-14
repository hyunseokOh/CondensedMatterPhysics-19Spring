import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,np.pi,10000)

m=1
M=2
w0=np.sqrt((M+m)/(M*m)+np.sqrt(M*M+m*m+2*M*m*np.cos(0))/(M*m))
y1=np.sqrt((M+m)/(M*m)+np.sqrt(M*M+m*m+2*M*m*np.cos(x))/(M*m))/w0
y2=np.sqrt((M+m)/(M*m)-np.sqrt(M*M+m*m+2*M*m*np.cos(x))/(M*m))/w0

fig,ax=plt.subplots(figsize=(8,8))
ax.plot(x,y1)
ax.plot(x,y2)
ax.set_title(r"Frequency Dispersion of 1D diatomic chain")
ax.set_xlabel(r"$qa$")
ax.set_ylabel(r"$w/w0$")
ax.set_xlim(0,np.pi)
ax.set_ylim(0,1)
ax.legend(["Optical branch","Acoustic branch"])
ax.set_xticks([0,np.pi])
ax.set_xticklabels(["0",r"$\pi$"])
fig.savefig("1-c.png")

print(y2[-1]-y1[-1])

