
# LC - 59. Spiral Matrix II


n = 3

matrix = [[False for i in range(3)] for j in range(n)]

a = [[1,2,3],[8,9,4],[7,6,5]]

def visit(m):
    return m and [*m.pop(0)] + visit([*zip(*m)][::-1])

print(visit(a))
















#LC 290 - Word pattern - uber mock
# pattern = "deadbeef"
# str = "d e a d b e e f"
#
# str = str.split(' ')
# s = set(str)
# # print(s)
#
#
# print(set(pattern))
#
# if (len(pattern)!=len(str)) or len(set(pattern)) != len(s):
#     print(False)
#
#
#
# d = {}
# for i,val in zip(pattern,str):
#     if i not in d.keys():
#         d[i] = set([val])
#         continue
#     d[i].add(val)
#     if len(d[i]) > 1:
#         print(False)
#
# print(d)
#
# print(True)






# LC - 593. Valid Square
# p1 = [0,0]
# p2 = [1,1]
# p3 = [1,0]
# p4 = [0,1]
# import math
#
# def squaredist(a,b):
#     return (math.sqrt((b[1]-a[1])**2 + (b[0]-a[0])**2))
#
# ls = [squaredist(p1,p2),squaredist(p1,p3),squaredist(p1,p4),squaredist(p2,p3),squaredist(p2,p4),squaredist(p4,p3)]
# ls.sort()
# if ls[0] == ls[1] == ls[2] == ls[3]:
#     if ls[5] == ls[6]:
#         return True
#
# return False


