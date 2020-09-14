import numpy as np
#
# a = np.arange(12).reshape(3, 4)
# # print(a)
# # [[ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]]
#
# a_del = np.delete(a, 1, 1)
# print(a_del)
# # [[ 0  1  2  3]
#  [ 8  9 10 11]]

# print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
A=[[1,2],[3,4]]
y=[[5],[6]]
print(np.concatenate((A, y)))
