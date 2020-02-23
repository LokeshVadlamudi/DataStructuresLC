













# LC - 364. Nested List Weight Sum II
# nestedList = [[],[],[]]
#
#
# class Solution:
#     def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:


#better solution
            # unweighted = 0
            # weighted = 0
            # while nestedList:
            #     nextLevel = []
            #     for i in nestedList:
            #         if i.isInteger():
            #             unweighted += i.getInteger()
            #         else:
            #             nextLevel.extend(i.getList())
            #     weighted += unweighted
            #     nestedList = nextLevel
            # return weighted




# average solution
#         from collections import defaultdict
#         d = defaultdict(list)
#
#         if len(nestedList) == 0:
#             return 0
#
#         def go(p, c, dic):
#             for q in p.getList():
#                 if q.isInteger():
#                     dic[c].append(q)
#                 else:
#                     go(q, c + 1, dic)
#
#         for i in nestedList:
#             if i.isInteger():
#                 d[1].append(i)
#             else:
#                 count = 2
#                 go(i, count, d)
#         if d:
#             maxKey = max(d.keys()) + 1
#
#         total = 0
#         for i in d.keys():
#             for j in d[i]:
#                 total = total + j.getInteger() * abs(maxKey - i)
#         return (total)

#100. Same Tree

# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if p and q:
#             return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
#         return p is q

# solution 2/
# if not p and not q:
#     return True
# if not q or not p:
#     return False
# if p.val != q.val:
#     return False
# return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)


#solution iterative
# def check(p, q):
#     if not p and q is None:
#         return True
#     if not p or not q:
#         return False
#     if p.val != q.val:
#         return False
#     return True
#
#
# deq = deque([(p, q), ])
# while deq:
#     p, q = deq.popleft()
#     if not check(p, q):
#         return False
#     if p:
#         deq.append((p.left, q.left))
#         deq.append((p.right, q.right))
# return True









# 41. First Missing Positive
# nums = [1,3,4,5,6]
# n = len(nums)
#
# for i in range(n):
#     if nums[i] < 0 or nums[i] == 0 or nums[i] > n:
#         nums[i] = 1
# print(nums)
#
#
# for i in range(n):
#     ele = abs(nums[i])
#     if ele == n:
#         nums[0] = - abs(nums[0])
#     else:
#         nums[ele] = -abs(nums[ele])
# print(nums)







# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         if len(nums)==0:
#             return 1
#         d = {}
#         for i,val in enumerate(nums):
#             if val > 0:
#                 d[val] = i
#
#         if nums and max(nums) > 0:
#             for i in range(1,max(nums)):
#                 if i not in d.keys():
#                     return (i)
#             return(max(nums)+1)
#         else:
#             return 1











