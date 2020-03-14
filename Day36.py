# 108. Convert Sorted Array to Binary Search Tree
# nums = [-10,-3,0,5,9]
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         if not nums:
#             return None
#         mid = len(nums)//2
#         root = TreeNode(nums[mid])
#         root.left = self.sortedArrayToBST(nums[:mid])
#         root.right = self.sortedArrayToBST(nums[mid+1:])
#         return root

# 658. Find K Closest Elements
# arr = [1,2,3,4,5]
# k=4
# x=3
# left , right = 0 , len(arr) - k
#
# while left < right:
#     mid = (left + right) // 2
#     if x - arr[mid] > arr[mid + k] - x:
#         left = mid + 1
#     else:
#         right = mid
#
# print(arr[left:left + k])




