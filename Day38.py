# 680. Valid Palindrome II
# from collections import Counter
# s = "abca"
#
# l, r = 0, len(s) - 1
#
# while l < r:
#     if s[l] != s[r]:
#         one, two = s[l:r] , s[l+1:r+1]
#         print(one == one[::-1] or two == two[::-1])
#     l, r = l+1, r-1
# print(True)


# def rev(a):
#     sr = ''
#     for i in a:
#         sr = i + sr
#     return sr
#
#
# s1 = rev(s)
#
# if s1 == s:
#     print('True')
# else:
#     c = Counter(s1)
#     count = 0
#     for key in c.keys():
#         if c[key] == 1:
#             count += 1
#     if count > 2:
#         print(False)
# print(True)

# 252. Meeting Rooms
# intervals = [[0,30],[5,10],[15,20]]
#
# a = float('-inf')
#
#
# for i in sorted(intervals):
#     if a > i[0]:
#         print(False)
#     a = max(a,i[1])
#
# print(True)


# 448. Find All Numbers Disappeared in an Array

# nums = [4,3,2,7,8,2,3,1]
# miss = set()
# for i in range(len(nums)):
#     miss.add(i + 1)
# nums = set(nums)
#
# return miss - nums



















