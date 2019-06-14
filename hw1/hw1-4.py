import numpy as np
import matplotlib.pyplot as plt

def diff(a,b,thres):
    if np.abs(a-b)<thres:
        return True
    else:
        return False

def f(x,beta):
    return np.cos(x)+beta*np.sin(x)/x

N=100000
thres=1e-3
z=np.linspace(thres,10*np.pi,N)

betaLst=[0,0.25]

for beta in betaLst:
    bound_up=[]
    bound_down=[]
    uplock=True
    downlock=False
    upcount=0
    downcount=1
    prev=0

    for x in z:
        val=f(x,beta)

        if diff(val,1,thres) and val<1 and uplock:
            if upcount%2==0 and prev>val:
                bound_up.append(x)
                uplock=False
                downlock=True
                upcount+=1
            elif upcount%2==1:
                bound_up.append(x)
                upcount+=1
        
        if diff(val,-1,thres) and val>-1 and downlock:
            if downcount%2==0 and prev<val:
                bound_down.append(x)
                downlock=False
                uplock=True 
                downcount+=1
            elif downcount%2==1:
                bound_down.append(x)
                downcount+=1

        prev=val

    band1=np.linspace(bound_up[0],bound_down[0],N)
    band1_k=np.arccos(f(band1,beta))

    band2=np.linspace(bound_up[1],bound_down[1],N)
    band3=np.linspace(bound_up[2],bound_down[2],N)

    band1_inv=(band1*-1)[::-1]
    band2_inv=(band2*-1)[::-1]
    band3_inv=(band3*-1)[::-1]
    band1_k_inv=(band1_k*-1)[::-1]

    band1=np.hstack([band1_inv,band1])
    band2=np.hstack([band2_inv,band2])
    band3=np.hstack([band3_inv,band3])
    band1_k=np.hstack([band1_k_inv,band1_k])

    energy1=band1*band1
    energy2=band2*band2
    energy3=band3*band3

    fig,ax=plt.subplots(figsize=(8,8))
    ax.plot(band1_k,energy1)
    ax.plot(band1_k,energy2)
    ax.plot(band1_k,energy3)
    ax.set_title(r"Energy Dispersion for $\beta$=%.2lf" % beta)
    ax.set_xlabel(r"Wavevector $k$ * lattice constant $a$")
    ax.set_ylabel("Energy units of $\epsilon_0$")
    ax.set_xlim((-np.pi,np.pi))
    ax.set_ylim((0,None))

    fig.savefig("result_beta_%.2lf.png" % beta)

    print(bound_up)
    print(bound_down)

plt.show()

