# LC - 78. Subsets
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         subs = [[]]
#         for i in nums:
#             for x in range(len(subs)):
#                 ele = subs[x]
#                 subs.append(ele+[i])
#         return subs


# LC - 138. Copy List with Random Pointer
# class Solution:
#     def __init__(self):
#         self.dh = {}
#
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         if head == None:
#             return None
#         if head in self.dh:
#             return self.dh[head]
#         node = Node(head.val, None, None)
#         self.dh[head] = node
#         node.next = self.copyRandomList(head.next)
#         node.random = self.copyRandomList(head.random)
#         return node

# LC - 287. Find the Duplicate Number

# nums.sort()
# for i in range(len(nums)):
#     if nums[i] == nums[i-1]:
#         return nums[i]


# d = {}
# for i in nums:
#     if i not in d:
#         d[i] = True
#     else:
#         return i


# # LC - 153. Find Minimum in Rotated Sorted Array
# nums = [3,4,5,1,2]
# # nums = [1,2,3]
#
#
# if nums[-1] < nums[0]:
#     l = 0
#     r = len(nums)-1
#     while l <= r:
#         mid = l+(r-l)//2
#         if nums[mid] > nums[mid+1]:
#             print(nums[mid+1])
#         elif nums[mid-1] > nums[mid]:
#             print(nums[mid])
#         elif nums[mid] > nums[0]:
#             l = mid + 1
#         else:
#             r = mid - 1
#
# else:
#     print(nums[0])


















