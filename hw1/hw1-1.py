import numpy as np

def f(x):
    return 2*np.tanh(x)

def calc(alpha):
    init=1.9
    count=0
    threshold=0.00001
    while True:
        count+=1
        error=np.abs(init-f(init))
        
        if error<threshold:
            break
        else:
            init=alpha*f(init)+(1-alpha)*init
    
    
    print(init)
    print(error)
    print(count)

calc(0.5)
calc(0.01)
