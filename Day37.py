# 82. Remove Duplicates from Sorted List II

# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         dummy = ListNode(-1)
#         dummy.next = head
#         prev, curr = dummy, dummy.next
#
#         while curr:
#             if curr.next and curr.val == curr.next.val:
#                 valToRem = curr.val
#
#                 while curr and curr.val == valToRem:
#                     curr = curr.next
#                 prev.next = curr
#             else:
#                 prev, curr = curr, curr.next
#         return dummy.next





# 5356. Lucky Numbers in a Matrix

# matrix = [[7,8],[1,2]]
# # res = []
# # for i in (zip(*matrix)):
# #     val = max(i)
# #     for j in matrix:
# #         val1 = min(j)
# #         if val1 == val:
# #             res.append(val)

#5357. Design a Stack With Increment Operation
# class CustomStack:
#
#     def __init__(self, maxSize: int):
#         self.LenStack = maxSize
#         self.stack = []
#
#     def push(self, x: int) -> None:
#         if len(self.stack) == self.LenStack:
#             return
#         self.stack.append(x)
#
#     def pop(self) -> int:
#         if self.stack:
#             a = self.stack[-1]
#             self.stack = self.stack[:-1]
#             return a
#         return -1
#
#     def increment(self, k: int, val: int) -> None:
#         if k >= self.LenStack:
#             for i in range(len(self.stack)):
#                 self.stack[i] = self.stack[i] + val
#             return
#
#         for i in range(len(self.stack)):
#             if k > 0:
#                 self.stack[i] = self.stack[i] + val
#                 k -= 1
#                 continue
#             break
#
#         return


# 5179. Balance a Binary Search Tree
# class Solution:
#     def balanceBST(self, root: TreeNode) -> TreeNode:
#
#         def makeAlist(root, nodeList):
#             if not root:
#                 return
#             makeAlist(root.left, nodeList)
#             nodeList.append(root)
#             makeAlist(root.right, nodeList)
#
#         def BstBuilder(nodes, start, end):
#             if start > end:
#                 return None
#             mid = (start + end) // 2
#             node = nodes[mid]
#
#             node.left = BstBuilder(nodes, start, mid - 1)
#             node.right = BstBuilder(nodes, mid + 1, end)
#             return node
#
#         def buildTree(root):
#             nodes = []
#             makeAlist(root, nodes)
#             n = len(nodes)
#             return BstBuilder(nodes, 0, n - 1)
#
#         return buildTree(root)








