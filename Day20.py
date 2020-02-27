












# 107. Binary Tree Level Order Traversal II
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         res = []
#         level = [root]
#         while level:
#             res.append([i.val for i in level])
#             tmp = []
#             for i in level:
#                 tmp.extend([i.left, i.right])
#             level = [i for i in tmp if i]
#
#         res.reverse()
#
#         return res







# 199. Binary Tree Right Side View
# class Solution:
#     def rightSideView(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
#         ans = [root.val]
#         left = ans + self.rightSideView(root.left)
#         right = ans + self.rightSideView(root.right)
#         if len(right) >= len(left):
#             return right
#         return right + left[len(right):]




# 102. Binary Tree Level Order Traversal
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         # from collections import deque
#         level = [root]
#         res = []
#         while level:
#             res.append([i.val for i in level])
#             temp = []
#             for i in level:
#                 temp.extend([i.left,i.right])
#             level = [i for i in temp if i]
#         return res





# 429. N-ary Tree Level Order Traversal

# class Solution:
#     def levelOrder(self, root: 'Node') -> List[List[int]]:
#         if not root:
#             return []
#         res = []
#         queue = collections.deque([root])
#         while queue:
#             level = []
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 level.append(node.val)
#                 queue.extend(node.children)
#             res.append(level)
#         return res










# 112. Path Sum

# class Solution:
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         if not root:
#             return False
#         if not root.left and not root.right and root.val == sum:
#             return True
#         sum -= root.val
#         return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)







# 437. Path Sum III
# class Solution:
#     def pathSum(self, root: TreeNode, s: int) -> int:
#         finCount = 0
#
#         if root:
#             finCount += self.helper(root, s)
#             finCount += self.pathSum(root.left, s)
#             finCount += self.pathSum(root.right, s)
#         return finCount
#
#         pass
#
#     def helper(self, root, s):
#         count = 0
#         if root:
#             if root.val == s:
#                 count += 1
#             count += self.helper(root.left, s - root.val)
#             count += self.helper(root.right, s - root.val)
#         return count