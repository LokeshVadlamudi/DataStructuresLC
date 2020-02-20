
# LC - 739. Daily Temperatures

# T = [73, 74, 75, 71, 69, 72, 76, 73]
#
# res = []
# for i in range(len(T)-1):
#     t1 = T[i]
#     flag = True
#     for j in range(i+1,len(T)):
#         if T[j] > t1:
#             res.append(j-i)
#             flag = False
#             break
#     if flag:
#         res.append(0)
# res.append(0)
#
# print(res)




















# LC - 735. Asteroid Collision


# asteroids = [10,2,-5]
# res = []






# def goGood(ast):
#     for i in ast:
#         if len(res) == 0:
#             res.append(i)
#             continue
#         a = res[-1]
#         if i > 0 and a > 0:
#             res.append(i)
#             continue
#         if a > 0 and i < 0:
#             if abs(i) == abs(a):
#                 res.pop()
#                 continue
#             elif abs(i) > abs(a):
#                 res.pop()
#                 res.append(i)
#                 continue
#             else:
#                 continue
#         if a < 0 and i < 0:
#             res.append(i)
#             continue
#         if a < 0 and i > 0:
#             res.append(i)
#             continue
#     return (res)
#
# result = goGood(asteroids)
#
# print(result)




# LC - 124. Binary Tree Maximum Path Sum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def maxPathSum(self, root: TreeNode) -> int:
#         _, s = self.maxPsum(root)
#         return s
#
#     def maxPsum(self, root):
#         if root is None:
#             return (0, 0)
#         leftMaxSumAsBranch, leftMaxPathSum = self.maxPsum(root.left)
#         rightMaxSumAsBranch, rightMaxPathSum = self.maxPsum(root.right)
#         maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)
#
#         value = root.val
#         maxSumAsBranch = max(maxChildSumAsBranch + value, value)
#         maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch)
#         maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)
#         return (maxSumAsBranch, maxPathSum)
