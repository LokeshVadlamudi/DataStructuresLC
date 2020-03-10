# 1370. Increasing Decreasing String
# s = "aaaabbbbcccc"
# res = ''
# from collections import Counter
# c = Counter(s)
# s1 = sorted(c.keys())
# s2 = reversed(sorted(c.keys()))
#
# asc = True
# while c:
#     for i in s1 if asc else s2:
#         if c[i] > 0:
#             print(12)
#             res += i
#             c[i] -= 1
#             if c[i] == 0:
#                 del c[i]
#     asc = not asc
# print(res)

# 75. Sort Colors
c = 0
nums = [2,0,2,1,1,0]
# for i in range(len(nums)):
#     if nums[i] == 0:
#         nums[c] , nums[i] = nums[i] , nums[c]
#         c += 1
# for i in range(c,len(nums)):
#     if nums[i] == 1:
#         nums[c] , nums[i] = nums[i] , nums[c]
#         c += 1
# for i in range(c,len(nums)):
#     if nums[i] == 2:
#         nums[c] , nums[i] = nums[i] , nums[c]
#         c += 1







