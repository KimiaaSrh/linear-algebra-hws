lines = []
file1 = open('linear_solve.txt', 'r')
lines=file1.readlines()

# lineCounter=0
# numsArr=[]
# dimOfSamples=[]
# dimOfSamplesIndex=0
# i=0
# numsCounter=0
# while(lineCounter<len(lines)):
#     if(len(lines[lineCounter])==1):
#         print("oooooooooooooooooooooooooo")
#         print(i)
#         # dimOfSamples[i]=int(lines[lineCounter])
#         i=i+1
#         dimOfSamplesIndex=dimOfSamplesIndex+1
#     else:
#         var=[]
#         var=lines[lineCounter].split(" ")
#         for value in var:
#             numsArr[numsCounter]=float(value)
#             numsCounter+=1
#     lineCounter=lineCounter+1
lines.pop()
print(len(lines))
print(lines)
