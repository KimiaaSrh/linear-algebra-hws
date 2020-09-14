'''
algorithm be in soorat hast ke ebteda 2 ta dadeye random bar midarim va bar asase fasele baghie noghat ba in 2 noghte,
cluster bandi mikonim , be in soorat ke age faselashoon az noghte aval kamtar bood dar cluster 1 va dar gheire in soorat,
dar cluster e 2 gharar migiran.
khob hala manteghan be in fekr mikonim ke mitunim cluster sazi ro ba maani tar konim, be in soorat ke,
miaim miangine har cluster ro migirim va dobare fasele tamame noghat ro ba in 2 adad dobare peida mikonim,
dobare cluster bandi mikonim va mibinim ke cluster ha update mishan.
enghad in kar ro edame midim ke dige 2 ta cluster ei ke jadid misazim ba 2 ta cluster ei ke dafe pish sakhtim farghi nadashte bashan.
(based on this link : https://www.datacamp.com/community/tutorials/k-means-clustering-python)

khob hala 2 ta cluster darim ke mikhaim bar asaseshun s ro peida konim, hala miaim faseleye 2 be 2 ye tamame noghat az guruh haye
mokhalef ro be dast miarim , maximum ehsun mishe s

baraye print kardan dar file: miaim tamame data ro check mikonim , age dar cluster 1 bood jelosh 1 minevesim, dar gheire in soorat 2
'''

import csv
from random import randrange
import sys

def dotProduct(vector1,vector2):
    i=0
    sum=0
    while(i<4):
        sum+=vector1[i]*vector2[i]
        i+=1
    return sum

def getCosineSimilarity(x,y):
     counter=0
     normOfX=0
     normOfY=0
     while(counter<4):
         normOfX+=x[counter]**2
         normOfY+=y[counter]**2
         counter+=1
     normOfX=float(normOfX**0.5)
     normOfY=float(normOfY**0.5)
     return float(dotProduct(x,y))/float(normOfX*normOfY)

def readFile():
    data2=[]
    with open('dataset.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))
        i=0
        while(i<len(data)):
            lst=data[i]
            data2.append([float(j) for j in lst])
            i+=1
    return data2

def getAverageOfColumn(matrix,colIndex):
    i=0
    sum=0
    while(i<len(matrix)):
        sum+=matrix[i][colIndex]
        i+=1
    # print(len(matrix))
    return float(sum)/float(len(matrix))

def getClustering(disArray,data):
    cluster1=[]
    cluster2=[]
    i=0
    while(i<len(disArray)):
        if(disArray[i][0]>disArray[i][1]):
            cluster1.append(data[i])
        else:
            cluster2.append(data[i])
        i+=1
    return cluster1,cluster2

def solve(data):

    distancesArray=[[0 for x in range(4)] for y in range(len(data))]
    first=data[randrange(len(data)-1)]
    second=data[randrange(len(data)-1)]
    while(True):
        if(first==second):
            second=data[randrange(len(data)-1)]
        else:
            break
    i=0
    while(i<len(data)):
        distancesArray[i][0]=getCosineSimilarity(data[i],first)
        distancesArray[i][1]=getCosineSimilarity(data[i],second)
        i+=1
    cl1,cl2=getClustering(distancesArray,data)
    cl11=[]
    cl22=[]
    cl11=cl1
    cl22=cl2
    while(True):
        first=[getAverageOfColumn(cl11,0),getAverageOfColumn(cl11,1),getAverageOfColumn(cl11,2),getAverageOfColumn(cl11,3)]
        second=[getAverageOfColumn(cl22,0),getAverageOfColumn(cl22,1),getAverageOfColumn(cl22,2),getAverageOfColumn(cl22,3)]
        i=0
        while(i<len(data)):
            distancesArray[i][0]=getCosineSimilarity(data[i],first)
            distancesArray[i][1]=getCosineSimilarity(data[i],second)
            i+=1
        cl1,cl2=getClustering(distancesArray,data)
        if(cl1==cl11 and cl2==cl22):
            return cl1,cl2,first,second
        cl11=cl1
        cl22=cl2

def getTwinDistances(cl1,cl2):
    maxDistance=getCosineSimilarity(cl1[0],cl2[0])
    counter=0
    while counter<len(cl1):
        counter2=0
        while counter2<len(cl2):
            temp=getCosineSimilarity(cl1[counter],cl2[counter2])
            if(temp>maxDistance):
                maxDistance=temp
            counter2+=1
        counter+=1
    return maxDistance

def witeIntoOutputFile(data,cl1,cl2,s):
    with open('cosinesimilarity.txt', 'w') as the_file:
        i=0
        while(i<len(data)):
            if(data[i] in cl1):
                the_file.write('1\n')
            elif(data[i] in cl2):
                the_file.write('2\n')
            i+=1
        the_file.write('s is : ')
        the_file.write(str(s))

dataArray=readFile()
cluster1,cluster2,centroidOfCl1,centroidOfCl2=solve(dataArray)
s=getTwinDistances(cluster1,cluster2)
s=s-sys.float_info.epsilon
print('s is ',str(s))
witeIntoOutputFile(dataArray,cluster1,cluster2,s)
# print(len(cluster1))
# print(len(cluster2))
# print(centroidOfCl1)
# print(centroidOfCl2)
