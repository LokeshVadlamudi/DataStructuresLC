# nums = [5,3,3,5,1]
# index = [0,0,2,1,2]
#
# d = {}
#
# res = []
# for i , j in zip(nums,index):
#     # if j not in d:
#     #     res.append(i)
#     #     d[j] = True
#     # else:
#     res.insert(j,i)
#     print(res)
# print(res)
import math

def goGood(n) :
    i = 1
    res = []
    while i <= n :
        if (n % i==0) :
            res.append(i),
        i = i + 1
    return res

nums = [21,4,7]

total = 0
for i in nums:
    a = goGood(i)
    if len(a) == 4:
        total += sum(a)

print(total)





