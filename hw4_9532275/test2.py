import numpy as np
def back_substitution(R,qty) :
    n = len(R)
    x = [[0 for x in range(1)] for y in range(n)]

    x[n-1] = qty[n-1]/R[n-1, n-1]
    for i in range(n-2, -1, -1):
        bb = 0
        for j in range (i+1, n):
            bb += R[i, j]*x[j]

        x[i] = (qty[i]-bb)/R[i, i]

    return x

M = np.matrix([5,6])
c = np.matrix([[1, 2], [3,4]])
print(back_substitution(M,c))
#
# A=[[ 5. , 2. , 7.],[ 3. , 7., 10.],[11.,  8., 19.]]
# print(len(A))
