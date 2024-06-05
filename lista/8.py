import numpy as np

def func(x):
    f=1/(7-2*x)
    return f
def AREA(x):
    fi=0.5*np.log(7-2*x)
    return fi
A1=AREA(1)
A2=AREA(3)
A=A2-A1
x1=3
x0=1
fx0=func(x1)
fx1=func(x0)
T=[2,4,8,16,32,64]
for i in T:
    S=x0
    h=(x1-x0)/i
    fx=0
    
    

    for j in range(i-1):
        #print(f'{i} {j} ')
        
        #print(j)
        S+=h
        #print(f'{i} {S}')
        
        fx+= func(S)
        #print(fx)
    


    AT=h*(((fx0+fx1)/2)+fx)

    print(f'area de {i} trapezios é {AT}')
    print(f'erro absoluto é {AT-A}')