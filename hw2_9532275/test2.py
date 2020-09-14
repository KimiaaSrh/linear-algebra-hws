def getDisjointCycles(perm):
  remain = set(perm)
  result = []
  while len(remain) > 0:
    n = remain.pop()
    cycle = [n]
    while True:
      n = perm[n]
      if n not in remain:
        break
      remain.remove(n)
      cycle.append(n)
    result.append(cycle)
  return result
def fillTemp(inputDisCycles):
    temp = dict()
    counter=0
    while(counter<len(inputDisCycles)):
        size=len(inputDisCycles[counter])
        if size in temp:
            keys=temp[size]
            keys.append(inputDisCycles[counter])
            temp[size]=keys
        else:
            temp[size]=[0]
            keys=temp[size]
            keys.append(inputDisCycles[counter])
            temp[size]=keys
        counter+=1
    return temp
def checkIfSquareRootExists(inputDic):
    evenCounter=0
    for value in inputDic:
        if(value%2==0):
            evenCounter+=(len(inputDic.get(value))-1)
    if(evenCounter%2==0):
        return True
    return False
def getSquareRoot(inputDic):
    squareRootDic=dict()
    for value in inputDic:
        if(((len(inputDic.get(value))-1)%2)==0):
            i=2
            newKeys=[]
            sag=len(inputDic.get(value))-1
            while(i<=sag):
                var1=[]
                var2=[]
                var2=inputDic.get(value)[i]
                var1=inputDic.get(value)[i-1]
                res=[]
                j=0
                k=0
                for value in var1:
                    res.append(var1[j])
                    res.append(var2[j])
                    k+=1
                    j+=1
                i+=2
                newKeys.append(res)
            if value in squareRootDic:
                keys=squareRootDic[value]
                keys.append(newKeys)
                squareRootDic[value]=keys
            else:
                squareRootDic[value]=[0]
                keys=squareRootDic[value]
                keys.append(newKeys)
                squareRootDic[value]=keys
        elif((len(inputDic.get(value))-1)%2!=0 and value%2!=0 ):
            newKeys=[]
            k=1
            while(k<len(inputDic.get(value))):
                res=[]
                i=0
                j=0
                while(j<len(inputDic.get(value)[k])) :
                    res.append(inputDic.get(value)[k][j])
                    # print(int(len(inputDic.get(value)[k])/2))
                    if(j<len(inputDic.get(value)[k])/2-1):
                        res.append(inputDic.get(value)[k][j+int(len(inputDic.get(value)[k])/2+1)])
                    else:
                        break
                    j+=1
                # print(res)
                k+=1
                newKeys.append(res)
                # print(newKeys)
            if value in squareRootDic:
                keys=squareRootDic[value]
                keys.append(newKeys)
                squareRootDic[value]=keys
            else:
                squareRootDic[value]=[0]
                keys=squareRootDic[value]
                keys.append(newKeys)
                squareRootDic[value]=keys
        elif((len(inputDic.get(value))-1)%2!=0 and value%2==0 ):
            squareRootDic[value]=[0]
            keys=inputDic[value]
            squareRootDic[value]=keys
    return squareRootDic
def removeZeros(inputDic):
    for value in inputDic:
        values=inputDic.get(value)
        values.pop(0)
    listOfCycles=[]
    for value in inputDic:
        j=0
        k=0
        while(k<len(inputDic.get(value))):
            while(j<len(inputDic.get(value)[k])):
                new_list = [x[0] for x in inputDic.get(value)]
                listOfCycles.append(new_list)
                j+=1
            k+=1
    listOfCycles2=[]
    for value in listOfCycles:
        if(len(value)>1):
            for value2 in value:
                listOfCycles2.append(value2)
        else:
            listOfCycles2.append(value[0])
    return listOfCycles2
def convertCyclesToMatrix(inputList):
    output=dict()
    for value in inputList:
        counter=0
        while(counter<(len(value)-1)):
            # print("//////// \n")
            # print(value)
            # print(value[counter+1])
            # print(" \n")
            output[value[counter]]=value[counter+1]
            counter+=1
        output[value[counter]]=value[0]
    return output
def getMatrix(inputDic):
    A= [[0 for x in range(len(inputDic))] for y in range(len(inputDic))]
    for value in inputDic:
        A[value][inputDic.get(value)]=1
    return A


# file1 = open('data2.txt', 'r')
file1 = open('data.txt', 'r')
lines=file1.readlines()
samplesCounter=2
while(samplesCounter<len(lines)/2):
    # print("/////// \n")
    # print(samplesCounter)
    # print("/////// \n")
    cCoiunter=0
    list=[]
    while(cCoiunter<len(lines[samplesCounter].split(" "))):
        list.append(int(lines[samplesCounter].split(" ")[cCoiunter]))
        cCoiunter+=1
    perMatrix=tuple(list)
    # print(getDisjointCycles(perMatrix))
    disjointCycles=getDisjointCycles(perMatrix)
    # print(disjointCycles)
    seperatedDisjointCycles=fillTemp(disjointCycles)
    # print(seperatedDisjointCycles)
    if(checkIfSquareRootExists(seperatedDisjointCycles)):
        # print("square root dare ")
        result=getSquareRoot(seperatedDisjointCycles)
        cyclesOfRootedSquareMatrix=removeZeros(result)
        AdoDic=convertCyclesToMatrix(cyclesOfRootedSquareMatrix)
        # print(AdoDic)
        AdoMatrix=getMatrix(AdoDic)
        print(AdoDic)
    else:
        print("A does not exist.")
    samplesCounter+=2
# perMatrix=(3, 1, 7, 0, 6, 5, 8, 2, 4)
# perMatrix=(2,3,0,1)
# perMatrix=(1,2,0)
# perMatrix=(2,1,0)
