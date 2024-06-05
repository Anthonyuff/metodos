import numpy as np

def func(x):
    f=1/(7-2**x)
    return f
def AREA(x):
    fi=0.5*np.log(7-2*x)
    return fi
A1=AREA(1)
A2=AREA(3)
A=A2-A1

fx0=func(1)
fx1=func(3)
T=[2,4,8,16,32,64]
for i in T:
    h=(fx1-fx0)/i
    for j in range(i-1):
        S=fx0
        S+=h

    AT=h*(((fx0+fx1)/2)+S)

    print(f'area de {i} trapezios é {AT}')
    print(f'erro absoluto é {AT-A}')