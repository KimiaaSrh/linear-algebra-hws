def swap(a, b):
    temp = a
    a = b
    b = temp
def det(matrix,n):
    w, h = n, 1;
    temp = [[0 for x in range(w)] for y in range(h)]
    temp2 = [[0 for x in range(w)] for y in range(h)]
    i=0
    alpha=0
    pivotingCount=0
    while(i<n-1):
        j=i+1
        while(j<=n-1):
            if(matrix[j][i]!=0.0 and  matrix[i][i]!=0.0):
                alpha=float(matrix[j][i])/float(matrix[i][i])
                k=0
                while(k<n):
                    temp[0][k]=float(alpha*(float(matrix[i][k])))
                    temp2[0][k]=float(alpha*(float(uniqueMatrix[i][k])))
                    k=k+1
                c=0
                while(c<n):
                    matrix[j][c]=float(matrix[j][c])-float(temp[0][c])
                    #khate baadi baraye be dast avordane inverse e
                    uniqueMatrix[j][c]=float(uniqueMatrix[j][c])-float(temp2[0][c])
                    c=c+1
            elif(matrix[i][i]==0):
                pivotingCount=pivotingCount+1
                counter=i+1
                while(counter<n):
                    if(matrix[counter][i]!=0):
                        counter2=0
                        while(counter2<n):
                            var=matrix[counter][counter2]
                            matrix[counter][counter2]=matrix[i][counter2]
                            matrix[i][counter2]=var
                            # 3 khate baadi baraye be dast avordane inverse e
                            var=uniqueMatrix[counter][counter2]
                            uniqueMatrix[counter][counter2]=uniqueMatrix[i][counter2]
                            uniqueMatrix[i][counter2]=var
                            counter2=counter2+1
                    counter=counter+1
                j=j-1
            j=j+1
        i=i+1
    cp=0
    mul=1
    while(cp<n):
        mul=float(mul)*matrix[cp][cp]
        cp=cp+1
    print("the determinant is: "+str(mul-pivotingCount))
    print("\n")
    if(float(mul)!=0):
        inverse(matrix,n,uniqueMatrix)
    else:
        print("this matrix does not have inverse")

def inverse(matrix,n,uniqueMatrix):
    w, h = n, 1;
    temp = [[0 for x in range(w)] for y in range(h)]
    temp2 = [[0 for x in range(w)] for y in range(h)]
    i=n-1
    alpha=0
    while(i>=1):
        j=i-1
        while(j>=0):
            if(matrix[j][i]!=0.0 and  matrix[i][i]!=0.0):
                alpha=float(matrix[j][i])/float(matrix[i][i])
                k=0
                while(k<n):
                    temp[0][k]=float(alpha*(float(matrix[i][k])))
                    temp2[0][k]=float(alpha*(float(uniqueMatrix[i][k])))
                    k=k+1
                c=0
                while(c<n):
                    matrix[j][c]=float(matrix[j][c])-float(temp[0][c])
                    uniqueMatrix[j][c]=float(uniqueMatrix[j][c])-float(temp2[0][c])
                    c=c+1
            elif(matrix[i][i]==0):
                counter=i-1
                while(counter>=0):
                    if(matrix[counter][i]!=0):
                        counter2=0
                        while(counter2<n):
                            var=matrix[counter][counter2]
                            matrix[counter][counter2]=matrix[i][counter2]
                            matrix[i][counter2]=var
                            var=uniqueMatrix[counter][counter2]
                            uniqueMatrix[counter][counter2]=uniqueMatrix[i][counter2]
                            uniqueMatrix[i][counter2]=var
                            counter2=counter2+1
                        counter=counter-1
                j=j+1
            j=j-1
        i=i-1
    cc=0
    while(cc<n):
        if(matrix[cc][cc]!=1):
            xcount=0
            while(xcount<n):
                uniqueMatrix[cc][xcount]=float(uniqueMatrix[cc][xcount]*(float(1.0)/float(matrix[cc][cc])))
                xcount=xcount+1
        cc=cc+1
    # print(uniqueMatrix)
def solveEquation(uniqueMatrix,b,result):
    for i in range(len(uniqueMatrix)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += uniqueMatrix[i][k] * b[k][j]
    return result

def subtract(inp1,inp2,result3):
    for i in range(len(inp1)):
        for j in range(len(inp1[0])):
            result3[i][j] = inp1[i][j] - inp2[i][j]
    return result3

def normCalculator(input,n):
    i=0
    sum=0
    while(i<n):
        sum=sum+float(input[i][0]**2)
        i=i+1
    return sum**(float(1.0/2.0))
#####################
n=3
# matrix=[[2,1.2,2.9],[1.1,3.3,6.5],[3.7,2.3,1.3]]
matrix=[[1,3.2,1.9],[2.1,2.3,4.5],[6.7,2.3,4.3]]
mcopy=matrix
# matrix=[[25,5,1],[64,8,1],[144,12,1]]
# matrix=[[1,1,-1],[-1,-1,0],[1,0,-1]]
# matrix=[[1,1,1],[2,1,1],[1,1,2]]
# n=2
# matrix=[[1,3.2],[2.1,1.1]]
# matrix=[[1.2,1],[2,3.2]]
# b=[[1.6],[4.2]]
b=[[2],[1],[3]]
derivedX=[[0 for x in range(1)] for y in range(n)]
derivedB=[[0 for x in range(1)] for y in range(n)]
residual=[[0 for x in range(1)] for y in range(n)]
uniqueMatrix=[[0 for x in range(n)] for y in range(n)]
counn=0
while(counn<n):
    uniqueMatrix[counn][counn]=1
    counn=counn+1
det(matrix,n)
print("the inverse of matrix is: \n "+ str(uniqueMatrix))
print("\n")
solveEquation(uniqueMatrix,b,derivedX)
print("the derived x is: \n"+str(derivedX))
print("\n")
# matrix=[[2,1.2,2.9],[1.1,3.3,6.5],[3.7,2.3,1.3]]
matrix=[[1,3.2,1.9],[2.1,2.3,4.5],[6.7,2.3,4.3]]
# matrix=[[25,5,1],[64,8,1],[144,12,1]]
# matrix=[[1,3.2],[2.1,1.1]]
# matrix=[[1.2,1],[2,3.2]]
solveEquation(matrix,derivedX,derivedB)
print("the derived b is: \n"+str(derivedB))
print("\n")
subtract(derivedB,b,residual)
print("the residual vector is: \n "+ str(residual))
print("\n")
print("the norm of the residual vector is: "+ str(normCalculator(residual,n)))
