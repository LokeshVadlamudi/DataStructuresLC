
#LC - 332. Reconstruct Itinerary (uber mock)
# import collections
#
# tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
#
# #recursive method
# targets = collections.defaultdict(list)
#
# for a , b in sorted(tickets):
#     targets[a] += b,
#
# print(targets)
#
# t = {}
# for a,b in sorted(tickets)[::-1]:
#     if a in t.keys():
#         t[a].append(b)
#         continue
#     t[a] = [b]
# print(t)
#
# route = []
#
# def visit(airport):
#     while t[airport]:
#         visit(t[airport].pop())
#     route.append(airport)
# visit('JFK')
#
# print(route)
#








# 1st try
#
# d = {}
# for i in tickets:
#     if i[0] not in d:
#         d[i[0]] = [i]
#         continue
#     d[i[0]].append(i)
# res = []
# a = ['JFK']
# print(d)
# count = 0
# while a:
#     a1 = a.pop()
#     min1 = ['\u221e','\u221e']
#     for i in d[a1]:
#         min1 = min(i,min1)
#     print(min1)
#     count += 1
#     print(count)
#     if count == len(tickets):
#         for i in min1:
#             res.append(i)
#         break
#     d[a1] = [i for i in d[a1] if i != min1]
#
#     res.append(min1[0])
#     a.append(min1[1])
#     print(res)
#     print(a)
#     print(d)
#
# print(res)
#
#
#





# LC - 973. K Closest Points to Origin
# import math
# points = [[1,3],[-2,2]]
# K = 1
#
# d = {}
# dis = []
# res = []
#
# for i in points:
#     a = math.sqrt((i[1]-0)**2 + (i[0]-0)**2)
#     dis.append((a,i))
#
# dis = sorted(dis,key=lambda i:i[0])[:K]
# print([i[1] for i in dis])


# LC - 937. Reorder Data in Log Files

# logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
#
#
# df = []
# lf = []
# for i in logs:
#     # print(i)
#     id, res = i.split(' ', 1)
#     if res[0].isalpha():
#         df.append(i)
#         continue
#     lf.append(i)
#
#
# # print(df)
# df = [i.split(' ') for i in df]
# df = sorted(df,key=lambda i:i[1:])
#
# for i in range(len(df)-1):
#     if df[i][1:] == df[i+1][1:]:
#         df[i] , df[i+1] = df[i+1],df[i]
#
#
#
# df = [' '.join(i) for i in df]
# print(df+lf)


# print(df+logs)







# dl = []
#
# for i in logs:
#     a = i.split()[1]
#     if len(a) == 1:
#         dl.append(i)
#         logs.remove(i)
#
#
#
# print(dl)
# print(logs)
# logs = [i.split() for i in logs]
# logs = sorted(logs,key= lambda i:i[1:])
# logs = [' '.join(i) for i in logs]
#
#
# print(logs + dl)
#







# LC - 54. Spiral Matrix
# matrix = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
#
# print(matrix.pop(0))
# print([*zip(*matrix)][::-1])
#
#
# def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#     return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

# LC - 2. Add Two Numbers

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#
#         a = ''
#         b = ''
#         while l1 != None:
#             a = a + str(l1.val)
#             l1 = l1.next
#         while l2 != None:
#             b = b + str(l2.val)
#             l2 = l2.next
#         a = a[::-1]
#         b = b[::-1]
#         c = str(int(a) + int(b))[::-1]
#         n1 = ListNode(c[0])
#         c1 = n1
#         for i in c[1:]:
#             n1.next = ListNode(int(i))
#             n1 = n1.next
#         return c1

#LC - 1 two sum
# nums = [2, 7, 11, 15]
# target = 9
# d = {}
# for i in range(len(nums)):
#     if (target-nums[i]) in d.keys():
#         return [i,d[target-nums[i]]]
#     else:
#         d[nums[i]] = i


# LC - 34. Find First and Last Position of Element in Sorted Array
# import bisect
#
# nums = [5,7,7,8,8,10]
# target = 7
#
# i = bisect.bisect_left(nums,target)
# print(i,bisect.bisect(nums,target)-1) if i in nums[i:i+1] else [-1,-1]



# for i in range(len(nums)):
#     if nums[i] == target:
#         li = i
#         break
# for i in range(len(nums ) -1 ,-1 ,-1):
#     if nums[i] == target:
#         ri = i
#         return [li ,ri]
#
# return [-1 ,-1]













# LC - 33. Search in Rotated Sorted Array

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l = 0
#         r = len(nums) - 1
#
#         if len(nums) == 1 and target == nums[0]:
#             return 0
#
#         while l <= r:
#             mid = l + (r - l) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] >= nums[l]:
#                 if target >= nums[l] and nums[mid] > target:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#             else:
#                 if target <= nums[r] and target > nums[mid]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#         return -1
