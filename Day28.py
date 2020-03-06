# 98. Validate Binary Search Tree

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         return self.goGood(root, float('-inf'), float('inf'))
#
#     def goGood(self, root, minval, maxval):
#         if not root:
#             return True
#         if root.val <= minval or root.val >= maxval:
#             return False
#         return self.goGood(root.left, minval, root.val) and self.goGood(root.right, root.val, maxval)


# 322. Coin Change

# coins = [1, 2, 5]
# n = 11
# dp = [float('inf') for _ in range(n+1)]
# dp[0] = 0
# print(dp)
#
# for denoms in coins:
#     for amount in range(n+1):
#         if denoms <= amount:
#             dp[amount] = min(dp[amount],1+dp[amount-denoms])
# print(dp[n])
# print(dp)




















# 20. Valid Parentheses

# s = "()[]{}"
#
# a = []
#
# d = {')':'(',']':'[','}':'{'}
#
# ob = '({['
# cb = '}])'
# for char in s:
#     if char in ob:
#         a.append(char)
#     elif char in cb:
#         if len(a) == 0:
#             print(False)
#         if d[char] == a[-1]:
#             a.pop()
#         else:
#             print(False)
# print(len(a)==0)








