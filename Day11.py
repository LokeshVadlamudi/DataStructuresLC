

# 498 - Diagonal Traverse
#
# matrix = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# height = len(matrix) - 1
# width = len(matrix[0]) - 1
#
# result = [matrix[0][0]]
# row,col = 0,1
# goingDown = True
#
#
#
# def isOutOfBounds(row,col,height,width):
#     return row < 0 or row > height or col < 0 or col > width
#
#
# while not isOutOfBounds(row,col,height,width):
#     result.append(matrix[row][col])
#     if goingDown:
#         if col == 0 or row == height:
#             goingDown = False
#             if row == height:
#                 col += 1
#             else:
#                 row += 1
#         else:
#             row += 1
#             col -= 1
#     else:
#         if row == 0 or col == width:
#             goingDown = True
#             if col == width:
#                 row += 1
#             else:
#                 col += 1
#
#         else:
#             row -= 1
#             col += 1
#
# print(result)
#
#
#
#
#
#


# LC - 139. Word Break
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
#
# ok = [True]
#
# for i in range(1,len(s)+1):
#     ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
#     print(ok)
# print(ok[-1])



# for i in wordDict:
#     if i in s:
#         s = s.replace(i,'')
# if s == '':
#     print(True)
# else:
#     print(False)








# LC - 268. Missing Number


# nums = [9,6,4,2,3,5,7,0,1]
# nums = sorted(nums)
# for i,j in zip(range(len(nums)),nums):
#     if i != j:
#         print(i)


# missing = len(nums)
# for i, num in enumerate(nums):
#     missing ^= i ^ num
#
# return missing

# expected_sum = len(nums) * (len(nums) + 1) // 2
# actual_sum = sum(nums)
# return expected_sum - actual_sum












