# LC - 1007 Minimum Domino Rotations For Equal Row
from functools import reduce

A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
#
# for x in [A[0],B[0]]:
#     if all(x in d for d in zip(A,B)):
#         print(len(A) - max(A.count(x),B.count(x)))
# print(-1)

#solution 2
# s = reduce(set.__and__,[set(d) for d in zip(A, B)])
#
# x = s.pop()
# print(len(A) - max(A.count(x),B.count(x)))













# LC - 46 permutations

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         perms = []
#         self.helper(nums, [], perms)
#         return perms
#
#     def helper(self, array, cperm, perms):
#         if not len(array) and len(cperm):
#             perms.append(cperm)
#         else:
#             for i in range(len(array)):
#                 newarr = array[:i] + array[i + 1:]
#                 newperm = cperm + [array[i]]
#                 self.helper(newarr, newperm, perms)

#better solution

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         perms = []
#         self.helper(0, nums, perms)
#         return perms
#
#     def helper(self, i, arr, perms):
#         if i == len(arr) - 1:
#             perms.append(arr[:])
#         else:
#             for j in range(i, len(arr)):
#                 self.swap(arr, i, j)
#                 self.helper(i + 1, arr, perms)
#                 self.swap(arr, i, j)
#
#     def swap(self, array, i, j):
#         array[i], array[j] = array[j], array[i]





#LC 1192 - Critical connections in a network

# n = 4
# connections = [[0,1],[1,2],[2,0],[1,3]]
#
# from collections import Counter
#
# l = []
# for x in connections:
#     for j in x:
#         l.append(j)
#
#
# print(l)
# c = Counter(l)
#
# a = [i for i in c.keys() if min(c.values()) == c[i]]
# a = int("".join(map(str, a)))
# print([i for i in connections if i[0] == a or i[1] == a])






















# schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
#
# res = []
#
# for i in schedule:
#     res += [x for x in i]
#
# res = sorted(res,key=lambda i:i[0])
# print(res)
#
# schedule = []
# for i in res:
#     if schedule and i[0] <= schedule[-1][1]:
#         schedule[-1][1] = max(schedule[-1][1],i[1])
#     else:
#         schedule.append(i)
#
# print(schedule)
# res = []
# for i , j in zip(schedule,schedule[1:]):
#     res.append([i[1],j[0]])
# print(res)
#
#



