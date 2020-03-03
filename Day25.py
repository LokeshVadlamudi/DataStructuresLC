# 15. 3Sum


# nums = [-1, 0, 1, 2, -1, -4]
#
# res = []
# nums.sort()
#
# for i in range(len(nums)-1):
#     l = i + 1
#     r = len(nums)-1
#     while l < r:
#         if nums[i] + nums[l] + nums[r] == 0 and [nums[i],nums[l],nums[r]] not in res:
#             res.append([nums[i],nums[l],nums[r]])
#             while l<r and nums[l] == nums[l+1]:
#                 l+=1
#             while l<r and nums[r-1]==nums[r]:
#                 r-=1
#             l += 1
#             r -= 1
#         elif nums[i] + nums[l] + nums[r] < 0:
#             l += 1
#             continue
#         else:
#             r -= 1
#             continue
# print(res)





# 11. Container With Most Water

#
# heights = [1,8,6,2,5,4,8,3,7]
# l = 0
# r = len(heights)-1
# maxArea = 0
#
# while l<r:
#     minHeight = min(heights[l],heights[r])
#     maxArea = max(minHeight*(r-l),maxArea)
#     if heights[l] > heights[r]:
#         r -= 1
#         continue
#     else:
#         l += 1
# print(maxArea)

# 42. Trapping Rain Water

# heights =  [0,1,0,2,1,0,1,3,2,1,2,1]
# maxes = [0 for _ in heights]
#
# leftMax = 0
# for i in range(len(heights)):
#     height = heights[i]
#     maxes[i] = leftMax
#     leftMax = max(leftMax,height)
#
# rightMax = 0
# for i in reversed(range(len(heights))):
#     height = heights[i]
#     minHeight = min(rightMax,maxes[i])
#     if height < minHeight:
#         maxes[i] = minHeight - height
#     else:
#         maxes[i] = 0
#     rightMax = max(rightMax,height)
# print(sum(maxes))


















