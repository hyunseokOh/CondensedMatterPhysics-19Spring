import re
import numpy as np
import matplotlib.pyplot as plt

fr=open("data.dat",mode='r')

Nk=0
Nband=0
Ef=0

for i in range(11):
    s=fr.readline()
    if i==4:
        lst=re.findall("-?\d+",s)
        Ef=float(lst[0]+'.'+lst[1])

    if i==7:
        print(s)
        lst=re.findall("\d+",s)
        Nband=int(lst[0])
        Nk=int(lst[-1])

print(Ef)
print(Nk)
print(Nband)


x=np.zeros(Nk)
y=np.zeros((Nband,Nk))

Nplot=Nband

for i in range(Nband):
    for j in range(Nk):
        s1=fr.readline()
        lst=re.findall("-?\d+",s1)
        print(lst)
        x[j]=(float(lst[0]+'.'+lst[1]))
        y[i][j]=(float(lst[2]+'.'+lst[3]))-Ef
        
    fr.readline()
    fr.readline()


fig,ax=plt.subplots(figsize=(8,8))
for i in range(Nplot):
    ax.plot(x,y[i])

plt.show()
