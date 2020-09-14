



# A=[[-1,-1,1],[1,3,3],[-1,-1,5],[1,3,7]]
# A=[[1,-1,4],[1,4,-2],[1,4,2],[1,-1,0]]
# A=[[ 5. , 2. , 7.],[ 3. , 7., 10.],[11.,  8., 19.]]
# A=[[0.8, 0. , 0.5],[0.6, 0.5, 0.8], [0.9 ,0.5 ,0.4]]
# A=[[ 1. , 2., -4.],[ 3.,  4. ,-6.],[ 5. , 6., -8.]]
# A=[[1,2],[3,4]]
# y=[[0],[1],[2]]
# y=[[0.2],[0],[0.3]]
# y=[[-0.1],[2.5],[5.1]]
# y=[[5],[6]]
# def readfile():
#     with open('file') as f:
#     w, h = [int(x) for x in next(f).split()]
#     array = [[int(x) for x in line.split()] for line in f]
#     return array
#     counter=0
#     while(counter<len(lines)):



file1 = open('new.txt', 'r')
lines=file1.readlines()
counter=0
array=[]
while(counter<len(lines)):
    array.append(float(lines[counter].replace("\n","")))
    counter+=1
print(array)
