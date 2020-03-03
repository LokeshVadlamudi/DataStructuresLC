# 46. Permutations
# nums = [1,2,3]
#
# def helper(array,cperms,perms):
#     if not len(array) and len(cperms):
#         perms.append(cperms)
#     else:
#         for i in range(len(array)):
#             newarr = array[:i] + array[i+1:]
#             newperm = cperms + [array[i]]
#             helper(newarr,newperm,perms)
#
# perms = []
# helper(nums,[],perms)
# print(perms)

# 206. Reverse Linked List
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         p1 , p2 = None , head
#         while p2 != None:
#             p3 = p2.next
#             p2.next = p1
#             p1 = p2
#             p2 = p3
#         return p1













