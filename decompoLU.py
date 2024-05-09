import numpy as np

def decompoLU(A):
    n=A.shape[0]
    L=np.eye(n)
    U=np.zeros((n,n))
    for k in range(n):
        U[k, k:] = A[k, k:] - L[k, :k] @ U[:k, k:]
        L[(k+1):, k] = (A[(k+1):, k] - L[(k+1):, :] @ U[:, k]) / U[k, k]
    return L,U
def Y(L,b):
    n=len(b)
    y=np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - L[i, :i]@ y[:i]) / L[i, i]
    return y 
def X(U,y):
    n=len(y)
    x=np.zeros(n)
    for i in range(n-1, -1, -1):
        if U[i, i] == 0:
            
            print("A matriz U é singular. O sistema pode não ter solução única.")

            return None
        x[i] = (y[i] - U[i, i+1:] @ x[i+1:]) / U[i, i]
    return x 

#A=np.array([[5,2,1],[3,1,4],[1,1,3]])
A=np.array([[1,2,3],[4,5,6],[7,8,9]])

L,U=decompoLU(A)

#b=np.array([[0,-7,5]])

b=np.array([2,-1,1])

B=b.T

y=Y(L,B)

x=X(U,y)

print(x)
