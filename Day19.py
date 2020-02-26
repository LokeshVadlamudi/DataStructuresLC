# 349. Intersection of Two Arrays
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         ret = []
#         n1 = set(nums1)
#         n2 = set(nums2)
#         d = {}
#         for i in n1:
#             if i in n2:
#                 ret.append(i)
#         return ret


# 204. Count Primes
# n = 10
#
#
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         dp = [1] * (n)
#         if n == 0 or n == 1:
#             return 0
#         dp[0] = 0
#         dp[1] = 0
#         z = int(n ** 0.5) + 1
#         for i in range(2, z):
#             for j in range(2, n):
#                 # if  == 0:
#                 if i * j >= n:
#                     break
#                 dp[i * j] = 0
#
#         return sum(dp)


# 692. Top K Frequent Words
# import heapq
#
# words = ["i", "love", "leetcode", "i", "love", "coding"]
# k = 2
# from collections import Counter
# c = Counter(words)
#
# heap = []
#
# for i,val in c.items():
#     heap.append((-val,i))
#
# print(heap)
# heapq.heapify(heap)
# print(heap)
# r = []
# for i in range(k):
#     r.append(heapq.heappop(heap)[1])
#
# print(r)
#
#
#







#
#
# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         from collections import Counter
#         c = Counter(words)
#         t = list(c.items())
#
#         print(t)
#
#         t.sort(key=lambda i: (-i[1], i[0]))
#
#         res = []
#         c = 0
#         for i in t:
#             if c < k:
#                 res.append(i[0])
#             c += 1
#
#         return(res)

# 200. Number of Islands
# grid = [['1', '1', '1', '1', '0'],
# ['1', '1', '0', '1', '0'],
# ['1', '1', '0', '0', '0'],
# ['0', '0', '0', '0', '0']]
#
# for i in grid:
#     print(i)
#
# def search(grid,i,j):
#     if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] != '1':
#         return
#     grid[i][j] = '&'
#     search(grid,i+1,j)
#     search(grid,i-1,j)
#     search(grid,i,j-1)
#     search(grid,i,j+1)
#
#
# count = 0
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == '1':
#             search(grid,i,j)
#             count += 1
# print(count)
#









































