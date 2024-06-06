import numpy as np
x=np.array([-4,-1,0,2,3])
y=np.array([3,-1,0,1,2])
X=np.sum(x)
Y=np.sum(y)
X2=np.sum(x**2)
n=len(y)
YX=np.sum(x*y)
G=np.array([[X2,X],
           [X,n]])
GP=np.array([[YX],
            [Y]])
mmq=np.linalg.solve(G,GP)
print(f'então é uma eq {mmq[0]}x + {mmq[1]}')

