def det(matrix,n,uniqueMatrix):
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
    if(float(mul*(-1)**pivotingCount)!=0):
        return mul*(-1)**pivotingCount,uniqueMatrix
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
    return (uniqueMatrix)
def solveEquation(uniqueMatrix,b,result):
    for i in range(len(uniqueMatrix)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += uniqueMatrix[i][k] * b[k][j]
    return result
def subtract(inp1,inp2,result3):
    for i in range(len(inp1)):
        for j in range(len(inp1[0])):
            result3[i][j] = float(inp1[i][j]) - float(inp2[i][j])
    return result3
def normCalculator(input,n):
    i=0
    sum=0
    while(i<n):
        sum=sum+float(input[i][0]**2)
        i=i+1
    return sum**(float(1.0/2.0))


lines = []
while True:
    line = input()
    if line!="0":
        lines.append(line)
    else:
        break
loopcounter=0
while(loopcounter<len(lines)):
    nn=0
    arr=lines[loopcounter]
    if(len(arr)==1):
        arr=lines[loopcounter+1].split(" ")
        loopcounter2=0
        arrcounter=0
        n=int(lines[loopcounter])
        A=[[0 for x in range(n)] for y in range(n)]
        H=[[0 for x in range(n)] for y in range(n)]
        AA=[[0 for x in range(n)] for y in range(n)]
        HH=[[0 for x in range(n)] for y in range(n)]
        b=[[0 for x in range(1)] for y in range(n)]
        uniqueMatrixInputA=[[0 for x in range(n)] for y in range(n)]
        uniqueMatrixInputH=[[0 for x in range(n)] for y in range(n)]
        derivedX=[[0 for x in range(1)] for y in range(n)]
        derivedB=[[0 for x in range(1)] for y in range(n)]
        residual=[[0 for x in range(1)] for y in range(n)]
        nn=n
        counn=0
        while(counn<n):
            uniqueMatrixInputA[counn][counn]=1
            uniqueMatrixInputH[counn][counn]=1
            counn=counn+1
        while loopcounter2<n:
            loopcounter3=0
            while(loopcounter3<n):
                A[loopcounter2][loopcounter3]=float(arr[arrcounter])
                AA[loopcounter2][loopcounter3]=float(arr[arrcounter])
                loopcounter3+=1
                arrcounter+=1
            loopcounter2+=1
        arr=lines[loopcounter+2].split(" ")
        loopcounter2=0
        arrcounter=0
        while loopcounter2<n:
            loopcounter3=0
            while(loopcounter3<n):
                H[loopcounter2][loopcounter3]=float(arr[arrcounter])
                HH[loopcounter2][loopcounter3]=float(arr[arrcounter])
                loopcounter3+=1
                arrcounter+=1
            loopcounter2+=1
        arr=lines[loopcounter+3].split(" ")
        loopcounter2=0
        arrcounter=0
        while loopcounter2<n:
            loopcounter3=0
            while(loopcounter3<1):
                b[loopcounter2][loopcounter3]=float(arr[arrcounter])
                loopcounter3+=1
                arrcounter+=1
            loopcounter2+=1
    print("matrix A , H , b are below: ")
    print(A)
    print(H)
    print(b)
    print("\n")
    determinA,uniqueMatrixOUtA=det(A,n,uniqueMatrixInputA)
    Ainverse=inverse(A,n,uniqueMatrixOUtA)
    print("determinant of A is : "+str(determinA))
    print("the inverse of matrix A is : ")
    print(Ainverse)
    solveEquation(Ainverse,b,derivedX)
    solveEquation(AA,derivedX,derivedB)
    subtract(b,derivedB,residual)
    print("x for A: \n")
    print(derivedX)
    print("\n")
    print("b - Ax \n ")
    print(residual)
    print("||b-Ax||: "+ str(normCalculator(residual,nn)))
    print("\n")
    derivedX=[[0 for x in range(1)] for y in range(nn)]
    derivedB=[[0 for x in range(1)] for y in range(nn)]
    residual=[[0 for x in range(1)] for y in range(nn)]
    determinH,uniqueMatrixOUtH=det(H,n,uniqueMatrixInputH)
    Hinverse =inverse(H,n,uniqueMatrixOUtH)
    print("determinant of H is : "+str(determinH))
    print("\n")
    print("the inverse of matrix H is : ")
    print(Hinverse)
    solveEquation(Hinverse,b,derivedX)
    solveEquation(HH,derivedX,derivedB)
    subtract(b,derivedB,residual)
    print("x for H: \n")
    print(derivedX)
    print("\n")
    print("b - Hx \n ")
    print(residual)
    print("||b-Hx||: "+ str(normCalculator(residual,nn)))
    print("\n")
    loopcounter+=4
