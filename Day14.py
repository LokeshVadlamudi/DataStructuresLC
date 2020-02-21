# 735 - asteroid collision:

asteroids = [5, 10, 5,-5]

ans = []

for i in asteroids:
    while ans and i < 0 < ans[-1]:
        if ans[-1] < -i:
            ans.pop()
            continue
        elif ans[-1] == -i:
            ans.pop()
        break
    else:
        ans.append(i)


print(ans)






# LC - 11. Container With Most Water
# height = [1,8,6,2,5,4,8,3,7]
#
# l = 0
# r = len(height)-1
# maxArea = 0
#
# flag = True
#
# while l <= r:
#     minHeight = min(height[l],height[r])
#     maxArea = max(minHeight*(r-l),maxArea)
#     if height[l] > height[r]:
#         r -= 1
#         continue
#     else:
#         l += 1
#
# print(maxArea)



#

# chars =["a","a","b","b","c","c","c"]
#
# from collections import OrderedDict
#
# d = OrderedDict()
#
# for i in chars:
#     if i not in d:
#         d[i] = 1
#         continue
#     d[i] += 1
# print(d)
#
# for i in d.keys():
#     chars.remove(i)
#     if d[i] > 1:
#         chars.insert(0,d[i])
#     chars.insert(0,i)
#
# print(chars)










#739 daily temperature

# T = [73, 74, 75, 71, 69, 72, 76, 73]
#
# ans = [0] * len(T)
#
# stack = []
#
# for i,val in enumerate(T):
#     while stack and T[stack[-1]] < val:
#         cur = stack.pop()
#         ans[cur] = i - cur
#     stack.append(i)
#     print(stack)
#
# print(ans)




# LC - 34. Find First and Last Position of Element in Sorted Array

# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         finalRange = [-1, -1]
#         self.alterSearch(nums, target, 0, len(nums) - 1, finalRange, True)
#         self.alterSearch(nums, target, 0, len(nums) - 1, finalRange, False)
#         return finalRange
#
#     def alterSearch(self, nums, target, left, right, finalRange, goLeft):
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] > target:
#                 right = mid - 1
#             else:
#                 if goLeft:
#                     if mid == 0 or nums[mid - 1] != target:
#                         finalRange[0] = mid
#                         return
#                     else:
#                         right = mid
#                 else:
#                     if mid == len(nums) - 1 or nums[mid + 1] != target:
#                         finalRange[1] = mid
#                         return
#                     else:
#                         left = mid + 1
#













# # LC - 380. Insert Delete GetRandom O(1)
# class RandomizedSet:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.dict = {}
#         self.list = []
#
#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val in self.dict:
#             return False
#
#         self.dict[val] = len(self.list)
#         self.list.append(val)
#         return True
#
#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val in self.dict:
#             lastele, idx = self.list[-1], self.dict[val]
#             self.list[idx], self.dict[lastele] = lastele, idx
#
#             self.list.pop()
#             del self.dict[val]
#             return True
#         return False
#
#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         import random
#         return random.choice(self.list)






