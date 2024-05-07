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
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x 

A=np.array([[5,2,1],[3,1,4],[1,1,3]])
L,U=decompoLU(A)

print(L)
