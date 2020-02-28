# 101. Symmetric Tree

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         def isSym(l, r):
#             if l and r and l.val == r.val:
#                 return isSym(l.left, r.right) and isSym(l.right, r.left)
#             return l == r
#
#         return not root or isSym(root.left, root.right)

# 278. First Bad Version
# class Solution:
#     def firstBadVersion(self, n):
#         l = 1
#         r = n
#         while l < r:
#             mid = l + (r - l) // 2
#             if isBadVersion(mid) == False:
#                 l = mid + 1
#             else:
#                 r = mid
#
#         return l






