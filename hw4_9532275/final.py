import numpy as np
def getNorm(vector):
    norm=0
    i=0
    sum=0
    while(i<len(vector)):
        sum+=float(vector[i]*vector[i])
        i+=1
    return float(sum**(0.5))

def getQueue(A):
    numrows = len(A)
    numcols = len(A[0])
    Q=[[0 for x in range(numcols)] for y in range(numrows)]
    i=0
    q=0
    normOfTemp=0
    while(i<numcols):
        j=0
        temp=[[0 for x in range(1)] for y in range(numrows)]
        while(j<q):
            alpha=0
            counter=0
            while(counter<numrows):
                alpha+=Q[counter][j]*A[counter][i]
                counter+=1
            counter=0
            while(counter<numrows):
                temp[counter][0]+=alpha*Q[counter][j]
                counter+=1
            j+=1
        counter=0
        while(counter<numrows):
            temp[counter][0]=A[counter][i]-temp[counter][0]
            counter+=1
        counter=0
        while(counter<numrows):
            if(abs(temp[counter][0])<10**(-14)):
                temp[counter][0]=0.0
            counter+=1
        # print(temp)
        normOfTemp=getNorm([row[0] for row in temp])
        if(normOfTemp!=0):
            counter=0
            while(counter<numrows):
                Q[counter][i]=temp[counter][0]/normOfTemp
                counter+=1
        else:
            counter=0
            while(counter<numrows):
                Q[counter][i]=temp[counter][0]
                counter+=1
        i+=1
        q+=1

    return Q

def getTranspose(Q):
    numrows = len(Q)
    numcols = len(Q[0])
    QTranspose=[[0 for x in range(numrows)] for y in range(numcols)]
    counter=0
    while(counter<numrows):
        counter2=0
        while(counter2<numcols):
            QTranspose[counter2][counter]=Q[counter][counter2]
            counter2+=1
        counter+=1
    return QTranspose

def getR(X,Y):
    numrows = len(X)
    numcols = len(Y[0])
    result=[[0 for x in range(numrows)] for y in range(numcols)]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    counter=0
    while(counter<len(result)):
        counter2=0
        while(counter2<len(result[0])):
            if(abs(result[counter][counter2])<10**(-14)):
                result[counter][counter2]=0
            counter2+=1
        counter+=1
    return result

def mul(X,Y):
    numrows = len(X)
    numcols = len(Y[0])
    result=[[0 for x in range(numrows)] for y in range(numcols)]
    result=np.dot(X,Y)
    return result

def removeZeros(Q,A):
    numrows = len(Q)
    numcols = len(Q[0])
    deletedIndices=[]
    counter=0
    realCol=0
    while(counter<numcols):
        counter2=0
        zeroCounter=0
        while(counter2<numrows):
            if(Q[counter2][counter]==0.0):
                zeroCounter+=1
            counter2+=1
        if(zeroCounter==numrows):
            if(realCol not in deletedIndices):
                deletedIndices.append(realCol)
            Q=np.delete(Q, counter, 1)
            A=np.delete(A, counter, 1)
            numcols-=1
            counter-=1
        counter+=1
        realCol+=1
    return Q,A,deletedIndices

def back_substitution(R,qty) :
    n = len(R)
    x = [[0 for x in range(1)] for y in range(n)]

    x[n-1] = qty[n-1]/R[n-1][n-1]
    for i in range(n-2, -1, -1):
        bb = 0
        for j in range (i+1, n):
            bb += R[i][j]*x[j]

        x[i] = (qty[i]-bb)/R[i][i]

    return x

def getAugmentedA(A,y):
    numrows = len(A)
    numcols = len(A[0])
    augA=[[0 for x in range(numcols+1)] for y in range(numrows)]
    counter=0
    while(counter<numcols):
        counter2=0
        while(counter2<numrows):
            augA[counter2][counter]=A[counter2][counter]
            counter2+=1
        counter+=1
    # print(augA)
    counter=0
    while(counter<numrows):
        augA[counter][numcols]=y[counter][0]
        counter+=1

    return augA

def getColRank(input):
    numrows = len(input)
    numcols = len(input[0])
    counter=0
    deletedIndices=0
    while(counter<numcols):
        counter2=0
        zeroCounter=0
        while(counter2<numrows):
            if(input[counter2][counter]==0.0):
                zeroCounter+=1
            counter2+=1
        if(zeroCounter==numrows):
            deletedIndices+=1
        counter+=1
    return numcols-deletedIndices

def findError(A,x,y):
    yPrime=np.dot(A,x)
    err=[]
    counter=0
    while(counter<len(y)):
        err.append(y[counter]-yPrime[counter])
        counter+=1
    return err,getNorm(err)

A=[[1,2],[3,4]]
y=[[5],[6]]

queue=getQueue(A)
newQueue,newA,deletedColsIndices=removeZeros(queue,A)
queueTranspose=getTranspose(newQueue)
R=getR(queueTranspose,newA)
qtransmuly=mul(queueTranspose,y)
x=back_substitution(R,qtransmuly)
augmentedA=getAugmentedA(A,y)
queueOfAugmentedA=getQueue(augmentedA)
colRankOfAugmentedA=getColRank(queueOfAugmentedA)
colRankOfA=len(A[0])-len(deletedColsIndices)
numOfColsOfA=len(A[0])
xPrime=[]
if(len(deletedColsIndices)!=0):
    cc=0
    ccc=0
    while(cc<len(x)+len(deletedColsIndices)):
        if(cc in deletedColsIndices):
            xPrime.append(0)
        else:
            xPrime.append(x[ccc])
            ccc+=1
        cc+=1
else:
    xPrime=x
error,normOfError=findError(A,xPrime,y)
print('----------------- Q is ------------')
print()
for row in queue:
    print([str(x) for x in row])
print()
# print('----------------- Qtranspose * Y is ------------')
# print()
# for row in qtransmuly:
#     print([str(x) for x in row])
# print()
print('----------------- R is ------------')
print()
for row in R:
    print([str(x) for x in row])
print()
# print('-----------------Queue of  Augmented A is ------------')
# print()
# for row in queueOfAugmentedA:
#     print([str(x) for x in row])
# print()
# print('----------------- error is ------------')
# print()
# for row in error:
#     print([str(x) for x in row])
# print()
print('-----------------normOfError is ------------')
print()
print(normOfError)
print()

print("----------- solutions -----------")
if(colRankOfA<colRankOfAugmentedA):
    print('no solution')
    print()
elif(colRankOfA==numOfColsOfA):
    print('unique solution')
    print()
    print('----------------- x is ------------')
    print()
    for row in x:
        print([str(x) for x in row])
    print()
elif(colRankOfA<numOfColsOfA):
    print('these indices caused many solutions ',deletedColsIndices)
    print()
    print('many solution')
    print()
    # print('----------------- x is ------------')
    # print()
    # for row in x:
    #     print([str(x) for x in row])
    # print()
print()
