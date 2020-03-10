# 78. Subsets
# nums = [1,2,3]
# subs = [[]]
# for i in nums:
#     for x in range(len(subs)):
#         ele = subs[x]
#         subs.append(ele+[i])
#         print(subs)
# print(subs)



# 283. Move Zeroes
# nums = [0,1,0,3,12]
# count = 0
# for i in range(len(nums)):
#     if nums[i] != 0:
#         print(i,count)
#         nums[i], nums[count] = nums[count], nums[i]
#         count += 1
#         print(nums)
#
# print(nums)


# 198. House Robber

# nums = [1,2,3,1]
#
# dp = [0] * len(nums)
#
# if len(nums) == 0:
#     print(0)
# if len(nums) == 1:
#     print(nums[0])
# dp[0] = nums[0]
# dp[1] = max(nums[0],nums[1])
# for i in range(2,len(nums)):
#     dp[i] = max(dp[i-1],dp[i-2]+nums[i])
#
# print(dp[-1])













